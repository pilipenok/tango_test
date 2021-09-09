resource "google_redis_instance" "redis" {
  name           = "redis"
  memory_size_gb = 1
}
