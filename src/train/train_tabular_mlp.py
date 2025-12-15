import wandb
import pandas as pd
import numpy as np
import torch
import torch.nn as nn
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.impute import SimpleImputer
from sklearn.metrics import mean_squared_error

from src.datasets.load_predicts_tabular import load_predicts_extended
from src.models.mlp import MLP


def main():
    wandb.init(
        project="predicts-no-timewindow",
        group="tabular-mlp",
        name="mlp-baseline-logscaled",
        config={
            "target_transform": "log1p_species_richness",
            "model": "mlp",
            "data_level": "site",
            "features": "predicts_extended"
        }
    )

    wandb.define_metric("epoch"),
    wandb.define_metric("train_loss", step_metric="epoch"),
    wandb.define_metric("val_loss", step_metric="epoch"),

    df = load_predicts_extended()

    y = np.log1p(df["Species_richness"].values)

    categorical_cols = df.select_dtypes(include=["object"]).columns
    numeric_cols = (
        df.select_dtypes(exclude=["object"])
        .drop(columns=["Species_richness"])
        .columns
    )

    X_cat = pd.get_dummies(
        df[categorical_cols],
        dummy_na=True,
        drop_first=True
    )

    imputer = SimpleImputer(strategy="median")
    X_num = pd.DataFrame(
        imputer.fit_transform(df[numeric_cols]),
        columns=numeric_cols
    )

    X = pd.concat([X_num, X_cat], axis=1)

    wandb.log({
        "num_samples": len(X),
        "num_features": X.shape[1],
        "num_numeric_features": X_num.shape[1],
        "num_categorical_features": X_cat.shape[1],
    })

    X_train, X_temp, y_train, y_temp = train_test_split(
        X.values, y, test_size=0.3, random_state=42
    )

    X_val, X_test, y_val, y_test = train_test_split(
        X_temp, y_temp, test_size=0.5, random_state=42
    )

    scaler = StandardScaler()
    X_train = scaler.fit_transform(X_train)
    X_val = scaler.transform(X_val)
    X_test = scaler.transform(X_test)

    X_train = torch.tensor(X_train).float()
    y_train = torch.tensor(y_train).float()
    X_val = torch.tensor(X_val).float()
    y_val = torch.tensor(y_val).float()
    X_test = torch.tensor(X_test).float()
    y_test = torch.tensor(y_test).float()

    model = MLP(input_dim=X_train.shape[1])
    optimizer = torch.optim.Adam(model.parameters(), lr=1e-3)
    loss_fn = nn.SmoothL1Loss()

    for epoch in range(50):
        model.train()
        optimizer.zero_grad()

        preds = model(X_train).squeeze()

        weights = torch.expm1(y_train)
        weights = weights / weights.mean()

        loss = (weights * (preds - y_train) ** 2).mean()

        loss.backward()
        optimizer.step()


        model.eval()
        with torch.no_grad():
            val_preds = model(X_val).squeeze()
            val_loss = loss_fn(val_preds, y_val)

        wandb.log({
            "train_loss": loss.item(),
            "val_loss": val_loss.item(),
            "epoch": epoch
        })

    model.eval()
    with torch.no_grad():
        preds = model(X_test).squeeze()
        mse = mean_squared_error(y_test.numpy(), preds.numpy())
        rmse = mse ** 0.5

    wandb.log({
        "test_mse": mse,
        "test_rmse": rmse
    })

    y_true = np.expm1(y_test.numpy())
    y_pred = np.expm1(preds.numpy())
    residuals = y_true - y_pred

    plt.figure(figsize=(12, 12))
    plt.scatter(y_true, y_pred, alpha=0.3)
    lims = [y_true.min(), y_true.max()]
    plt.plot(lims, lims, linestyle="--")
    plt.xlabel("True species richness")
    plt.ylabel("Predicted species richness")
    plt.title("Predicted vs True")
    wandb.log({"predicted_vs_true": wandb.Image(plt)})
    plt.close()

    plt.figure(figsize=(12, 8))
    plt.scatter(y_true, residuals, alpha=0.3)
    plt.axhline(0, linestyle="--")
    plt.xlabel("True species richness")
    plt.ylabel("Residual")
    plt.title("Residuals vs True")
    wandb.log({"residuals_vs_true": wandb.Image(plt)})
    plt.close()

    plt.figure(figsize=(6,6))
    plt.scatter(y_test.numpy(), preds.numpy(), alpha=0.3)
    lims = [y_test.numpy().min(), y_test.numpy().max()]
    plt.plot(lims, lims, linestyle="--")
    plt.xlabel("True log1p(richness)")
    plt.ylabel("Pred log1p(richness)")
    plt.title("Predicted vs True (log scale)")
    wandb.log({"pred_vs_true_log": wandb.Image(plt)})
    plt.close()


    print("Test RMSE (log scale):", rmse)

    wandb.finish()


if __name__ == "__main__":
    main()
