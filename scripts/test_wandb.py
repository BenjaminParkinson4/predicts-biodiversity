import wandb
import time

#start wandb test
wandb.init(
    project="predicts-no-timewindow",
    entity="zm018645-university-of-reading",
    config={
        "test_run": True,
        "platform": "local/macJORJASMINORRACC"  #update per machine
    }
)

#log test values
for i in range(10):
    wandb.log({"test_metric": i})
    time.sleep(0.2)

wandb.finish()
