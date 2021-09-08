terraform {
  required_providers {
    google = {
      source  = "hashicorp/google"
      version = "3.5.0"
    }
  }
}

provider "google" {
  credentials = file("../../credentials.json")

  project = "myproject-311515"
  region  = "us-central1"
  zone    = "us-central1-c"
}

resource "google_compute_network" "vpc_network" {
  name = "terraform-network"
}

resource "google_sourcerepo_repository" "tango_test" {
  name = "tango_test"
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
