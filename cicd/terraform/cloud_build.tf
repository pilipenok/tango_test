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
    _REGION         = var.region
    _PROJECT_ID     = var.project
  }

  filename = "cicd/cloudbuild.yaml"
}
