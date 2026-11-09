# Configuración de OIDC con Azure y GitHub Actions

Para desplegar este contenedor automáticamente, puedes usar OpenID Connect (OIDC).

1. Crea una aplicación en Azure Entra ID (Active Directory).
2. Configura las credenciales federadas apuntando a tu repositorio de GitHub.
3. En tu GitHub Action, usa `azure/login@v1` con tu `client-id`, `tenant-id` y `subscription-id`.
