resource "google_bigtable_instance" "instance" {
  name = "tango-instance"

  cluster {
    cluster_id   = "tango-instance-cluster"
    num_nodes    = 1
    storage_type = "HDD"
  }

  labels = {
    my-label = "tango"
  }
}

resource "google_bigtable_table" "subscriptions" {
  name          = "subscriptions"
  instance_name = google_bigtable_instance.instance.name
  split_keys    = ["subscriber_id", "user_id", "timestamp"]

  lifecycle {
    prevent_destroy = true
  }
}