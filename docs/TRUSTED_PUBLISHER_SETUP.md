# PyPI Trusted Publisher Setup

This project uses PyPI Trusted Publisher for secure automated package publishing. This eliminates the need for long-lived API tokens and provides better security.

## What is Trusted Publisher?

Trusted Publisher uses OpenID Connect (OIDC) to exchange short-lived identity tokens between GitHub Actions and PyPI. This provides:

- **Better Security**: Tokens expire automatically after 15 minutes
- **Easier Setup**: No need to manually create and manage API tokens
- **Automated Authentication**: Seamless integration with CI/CD workflows

## Setup Instructions

### 1. Configure Trusted Publisher on PyPI

1. Go to your project page on PyPI
2. Navigate to "Settings" → "Trusted publishers"
3. Click "Add a new trusted publisher"
4. Configure the publisher with these settings:

**Publisher name**: `github-actions`
**Publisher specifier**: `github.com/rainx/cn_stock_holidays`
**Environment**: `ref:refs/tags/*`
**Workflow name**: `Test, Build & Publish`
**Workflow filename**: `.github/workflows/ci.yml`

### 2. CI Configuration

The CI workflow is already configured to use Trusted Publisher:

```yaml
publish:
  permissions:
    id-token: write # Required for Trusted Publisher authentication
  steps:
    - name: Publish to PyPI
      run: uv publish --yes
```

### 3. Publishing Process

1. Create and push a new tag:

   ```bash
   git tag v2.0.1
   git push origin v2.0.1
   ```

2. The CI workflow will automatically:
   - Run tests
   - Build the package
   - Publish to PyPI using Trusted Publisher authentication

## Security Benefits

- **Short-lived tokens**: Authentication tokens expire after 15 minutes
- **No manual token management**: No need to create, store, or rotate API tokens
- **Repository-specific**: Tokens are only valid for this specific repository
- **Environment restrictions**: Can be limited to specific branches or tags

## Troubleshooting

If publishing fails, check:

1. Trusted Publisher configuration on PyPI matches the repository
2. Workflow name and filename are correct
3. Environment specifier includes the tag pattern
4. Repository has the correct permissions

## References

- [PyPI Trusted Publishers Documentation](https://docs.pypi.org/trusted-publishers/)
- [GitHub Actions OIDC](https://docs.github.com/en/actions/deployment/security-hardening-your-deployments/about-security-hardening-with-openid-connect)
