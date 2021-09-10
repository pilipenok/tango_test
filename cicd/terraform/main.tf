terraform {
  required_providers {
    google = {
      source  = "hashicorp/google"
      version = "3.82.0"
    }

    google-beta = {
      source = "hashicorp/google-beta"
      version = "3.82.0"
    }
  }
}

provider "google" {
  credentials = file("../../credentials.json")

  project = var.project
  region  = var.region
  zone    = var.zone
}

provider "google-beta" {
  credentials = file("../../credentials.json")

  project = var.project
  region  = var.region
  zone    = var.zone
}

resource "google_storage_bucket" "bucket" {
  name = var.project
}

resource "google_pubsub_topic" "trigger-set-online" {
  name = "trigger-set-online"
}
