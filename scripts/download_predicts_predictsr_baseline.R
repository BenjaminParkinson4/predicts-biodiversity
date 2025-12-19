#using "predictsr" package
library(predictsr)
library(dplyr)

cat("Starting R script for loading PREDICTS dataset\n")

#get repo root based on the script location
args <- commandArgs(trailingOnly = FALSE)
file_arg <- "--file="
script_path <- sub(file_arg, "", args[grep(file_arg, args)])
repo_root <- normalizePath(file.path(dirname(script_path), ".."))

#project data paths
raw_dir <- file.path(repo_root, "src", "data", "raw", "predicts")
processed_dir <- file.path(repo_root, "src", "data", "processed")

dir.create(raw_dir, recursive = TRUE, showWarnings = FALSE)
dir.create(processed_dir, recursive = TRUE, showWarnings = FALSE)

#load full PREDICTS dataset
data <- GetPredictsData()
cat("Loaded full PREDICTS dataset with", nrow(data), "rows.\n")

#filter rows with valid species names
data_cleaned <- data %>% filter(!is.na(Species))
cat("Filtered dataset to", nrow(data_cleaned), "rows with valid species.\n")

#baseline site-level dataset
site_baseline <- data_cleaned %>%
  group_by(SS) %>%
  summarise(
    Species_richness = n_distinct(Species),
    LandUse = first(Predominant_land_use),
    Use_intensity = first(Use_intensity),
    Latitude = first(Latitude),
    Longitude = first(Longitude),
    .groups = "drop"
  )

write.csv(site_baseline, file.path(processed_dir, "predicts_cleaned.csv"), row.names = FALSE)
cat("Saved baseline site-level file: predicts_cleaned.csv\n")

#extended site-level dataset
site_extended <- data_cleaned %>%
  group_by(SS) %>%
  summarise(
    Species_richness = n_distinct(Species),
    LandUse = first(Predominant_land_use),
    Use_intensity = first(Use_intensity),
    Latitude = first(Latitude),
    Longitude = first(Longitude),

    #additional predictors
    Biome = first(Biome),
    Realm = first(Realm),
    Country = first(Country),
    Habitat = first(Habitat_as_described),
    Sampling_method = first(Sampling_method),
    Sampling_effort = first(Sampling_effort),
    Ecoregion = first(Ecoregion),
    Hotspot = first(Hotspot),
    Wilderness_area = first(Wilderness_area),

    .groups = "drop"
  )

write.csv(site_extended, file.path(processed_dir, "predicts_extended.csv"), row.names = FALSE)
cat("Saved extended site-level file: predicts_extended.csv\n")

#full cleaned species-level dataset (a direct cleaned export of all rows after filtering)
write.csv(data_cleaned, file.path(raw_dir, "predicts_raw_cleaned.csv"), row.names = FALSE)
cat("Saved full raw cleaned dataset: predicts_raw_cleaned.csv\n")

#comprehensive species-level dataset
#(rich flat table for future modelling time windows, GNNs, etc.)

comprehensive_dataset <- data_cleaned %>%
  select(
    #identifiers
    SS,
    SSS,
    Source_ID,

    #species information
    Species,

    #land-use and pressure variables
    Predominant_land_use,
    Use_intensity,
    Biome,
    Realm,
    Ecoregion,
    Habitat_as_described,

    #spatial information
    Latitude,
    Longitude,
    Country,

    #sampling information
    Sampling_method,
    Sampling_effort,

    #conservation / context flags
    Hotspot,
    Wilderness_area
  )

write.csv(comprehensive_dataset, file.path(processed_dir, "predicts_comprehensive.csv"), row.names = FALSE)
cat("Saved comprehensive dataset: data/processed/predicts_comprehensive.csv\n")

cat("All extraction tasks completed\n")
