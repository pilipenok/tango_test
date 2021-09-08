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

  project = var.project_id
  region  = var.region
  zone    = var.zone
}

provider "google-beta" {
  credentials = file("../../credentials.json")

  project = var.project_id
  region  = var.region
  zone    = var.zone
}

resource "google_compute_network" "vpc_network" {
  name = "terraform-network"
}

resource "google_artifact_registry_repository" "tango-test" {
    provider = google-beta
    location = var.region
    repository_id = "tango-test"
    format = "DOCKER"
}

resource "google_cloudbuild_trigger" "build-trigger" {
  github {
    owner = "pilipenok"
    name = "tango_test"
    push {
      branch = "master"
    }
  }

  substitutions = {
    _REGISTRY       = google_artifact_registry_repository.tango-test.repository_id
    _REGISTRY_URL   = "${var.region}-docker.pkg.dev"
  }

  filename = "cicd/cloudbuild.yaml"
}

//resource "google_cloud_run_service" "default" {
//  name     = "cloudrun-srv"
//  location = "us-central1"
//
//  template {
//    spec {
//      containers {
//        image = "us-docker.pkg.dev/cloudrun/container/hello"
//      }
//    }
//  }
//
//  traffic {
//    percent         = 100
//    latest_revision = true
//  }
//}
