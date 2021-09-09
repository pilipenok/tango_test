resource "google_compute_network" "vpc_network" {
  name = "terraform-network"
}

resource "google_vpc_access_connector" "vpc_connector" {
  name = "terraform-vpc-connector"

  network = google_compute_network.vpc_network.name
  region = var.region
  ip_cidr_range = "10.2.0.0/28"
}
