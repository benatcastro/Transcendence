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


// Nueva configuración para el archivo localhost.csr
template {
  source      = "/etc/consul-template/templates/localhost_csr.ctmpl"
  destination = "/output/localhost.csr"
  perms       = "0600"
}

// Nueva configuración para el archivo localhost.crt
template {
  source      = "/etc/consul-template/templates/localhost_crt.ctmpl"
  destination = "/output/localhost.crt"
  perms       = "0600"
}

