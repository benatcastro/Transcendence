vault {
  address = "http://vault:8200"
  token   = "myroot"
}

template {
  source      = "/consul-template/templates/mi-plantilla.tpl"
  destination = "/consul-template/output/mi-configuracion.conf"
  command     = "pkill -HUP myapp"
}

