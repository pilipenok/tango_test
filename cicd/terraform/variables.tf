variable "project" {
    default = "myproject-311515"
}

variable "region" {
    default = "us-central1"
}

variable "zone" {
    default = "us-central1-c"
}

variable "services" {
  type = list

  default = [
      "artifactregistry.googleapis.com",
      "cloudbuild.googleapis.com",
      "run.googleapis.com",
      "compute.googleapis.com",
      "logging.googleapis.com",
      "bigtableadmin.googleapis.com",
      "redis.googleapis.com",
      "vpcaccess.googleapis.com"
  ]
  description = "The GCP APIs that should be enabled in this project."
}