resource "google_redis_instance" "redis" {
  name           = "redis"
  memory_size_gb = 1

  location_id = var.zone
  authorized_network = google_compute_network.vpc_network.name
}
