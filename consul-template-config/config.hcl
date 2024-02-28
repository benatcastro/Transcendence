vault {
  address = "http://vault:8200"
  token   = "myroot"
  renew_token = false
}

template {
  source      = "/etc/consul-template/templates/env.ctmpl"
  destination = "/output/.env"
}

// Nueva configuración para el archivo localhost.key
template {
  source      = "/etc/consul-template/templates/localhost_key.ctmpl"
  destination = "/output/localhost.key"
  perms       = "0600"
}
