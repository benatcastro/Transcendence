#!/bin/ash
mkdir -p /etc/nginx/modsec
echo "# Include the recommended configuration
Include /etc/nginx/modsec/modsecurity.conf
# OWASP CRS v3 rules
Include /usr/local/owasp-modsecurity-crs-3.0.2/crs-setup.conf
Include /usr/local/owasp-modsecurity-crs-3.0.2/rules/REQUEST-900-EXCLUSION-RULES-BEFORE-CRS.conf
Include /usr/local/owasp-modsecurity-crs-3.0.2/rules/REQUEST-901-INITIALIZATION.conf
Include /usr/local/owasp-modsecurity-crs-3.0.2/rules/REQUEST-905-COMMON-EXCEPTIONS.conf
Include /usr/local/owasp-modsecurity-crs-3.0.2/rules/REQUEST-910-IP-REPUTATION.conf
Include /usr/local/owasp-modsecurity-crs-3.0.2/rules/REQUEST-911-METHOD-ENFORCEMENT.conf
Include /usr/local/owasp-modsecurity-crs-3.0.2/rules/REQUEST-912-DOS-PROTECTION.conf
Include /usr/local/owasp-modsecurity-crs-3.0.2/rules/REQUEST-913-SCANNER-DETECTION.conf
Include /usr/local/owasp-modsecurity-crs-3.0.2/rules/REQUEST-920-PROTOCOL-ENFORCEMENT.conf
Include /usr/local/owasp-modsecurity-crs-3.0.2/rules/REQUEST-921-PROTOCOL-ATTACK.conf
Include /usr/local/owasp-modsecurity-crs-3.0.2/rules/REQUEST-930-APPLICATION-ATTACK-LFI.conf
Include /usr/local/owasp-modsecurity-crs-3.0.2/rules/REQUEST-931-APPLICATION-ATTACK-RFI.conf
Include /usr/local/owasp-modsecurity-crs-3.0.2/rules/REQUEST-932-APPLICATION-ATTACK-RCE.conf
Include /usr/local/owasp-modsecurity-crs-3.0.2/rules/REQUEST-933-APPLICATION-ATTACK-PHP.conf
Include /usr/local/owasp-modsecurity-crs-3.0.2/rules/REQUEST-941-APPLICATION-ATTACK-XSS.conf
Include /usr/local/owasp-modsecurity-crs-3.0.2/rules/REQUEST-942-APPLICATION-ATTACK-SQLI.conf
Include /usr/local/owasp-modsecurity-crs-3.0.2/rules/REQUEST-943-APPLICATION-ATTACK-SESSION-FIXATION.conf
Include /usr/local/owasp-modsecurity-crs-3.0.2/rules/REQUEST-949-BLOCKING-EVALUATION.conf
Include /usr/local/owasp-modsecurity-crs-3.0.2/rules/RESPONSE-950-DATA-LEAKAGES.conf
Include /usr/local/owasp-modsecurity-crs-3.0.2/rules/RESPONSE-951-DATA-LEAKAGES-SQL.conf
Include /usr/local/owasp-modsecurity-crs-3.0.2/rules/RESPONSE-952-DATA-LEAKAGES-JAVA.conf
Include /usr/local/owasp-modsecurity-crs-3.0.2/rules/RESPONSE-953-DATA-LEAKAGES-PHP.conf
Include /usr/local/owasp-modsecurity-crs-3.0.2/rules/RESPONSE-954-DATA-LEAKAGES-IIS.conf
Include /usr/local/owasp-modsecurity-crs-3.0.2/rules/RESPONSE-959-BLOCKING-EVALUATION.conf
Include /usr/local/owasp-modsecurity-crs-3.0.2/rules/RESPONSE-980-CORRELATION.conf
Include /usr/local/owasp-modsecurity-crs-3.0.2/rules/RESPONSE-999-EXCLUSION-RULES-AFTER-CRS.conf" > /etc/nginx/modsec/main.conf
nginx -s reload