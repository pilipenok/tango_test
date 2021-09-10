resource "google_storage_bucket_object" "set_online_zip" {
  name = "set_online.zip"
  bucket = google_storage_bucket.bucket.name
  source = "./../../src/cf/set_online.zip"
  #content_type = "application/zip"
  #content_disposition = "attachment"
  #content_encoding    = "gzip"
  depends_on          = [ google_storage_bucket.bucket ]
}

resource "google_cloudfunctions_function" "set_online" {
  name        = "set-online"
  description = "populate redis with online users"
  runtime     = "python38"
  region = var.region
  available_memory_mb   = 128
  timeout               = 60
  entry_point           = "main"

  source_archive_bucket = google_storage_bucket_object.set_online_zip.bucket
  source_archive_object = google_storage_bucket_object.set_online_zip.name

  environment_variables = {
    REDIS_HOST = google_redis_instance.redis.host
    REDIS_PORT = google_redis_instance.redis.port
  }

  vpc_connector = google_vpc_access_connector.vpc_connector.name

  event_trigger {
    event_type = "google.pubsub.topic.publish"
    resource = google_pubsub_topic.trigger-set-online.name
  }
  depends_on          = [ google_storage_bucket_object.set_online_zip ]
}
