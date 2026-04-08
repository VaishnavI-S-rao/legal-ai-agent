# Docker Setup Guide - Legal Document Analyzer

## Overview

This guide provides comprehensive instructions for running the Legal Document Analyzer application using Docker. The application is containerized for easy deployment and consistent environment across different systems.

## Prerequisites

- **Docker Desktop** installed and running
- **Docker Compose** (included with Docker Desktop)
- **Git** for cloning the repository
- **At least 4GB of available RAM**
- **At least 10GB of available disk space**

## Quick Start

### 1. Clone the Repository
```bash
git clone <repository-url>
cd legal_document_analyzer
```

### 2. Environment Configuration

**Required for Superwise AI integration:**

Follow the environment setup steps to create your `.env` file with Superwise API credentials.

**Quick Reference:**
```bash
# Copy the example file
cp .env.example .env

# Edit with your Superwise API credentials
SUPERWISE_API_URL=https://api.superwise.ai/
SUPERWISE_API_VERSION=v1
SUPERWISE_APP_ID=YOUR_SUPERWISE_APP_ID
```

**Note**: The Superwise API configuration is optional for demo purposes. The application includes mock AI analysis for demonstration.

### 3. Using Docker Compose
```bash
# Build and start the application
docker-compose up --build

# Or run in detached mode
docker-compose up --build -d
```

### 4. Access the Application
- **URL**: http://localhost:9000
- **Health Check**: http://localhost:9000/_stcore/health

## Docker Configuration

### Docker Compose Services

The application uses a single service configuration:

```yaml
services:
  legal-analyzer:
    build: .
    ports:
      - "9000:9000"
    environment:
      - SUPERWISE_API_URL=${SUPERWISE_API_URL}
      - SUPERWISE_API_VERSION=${SUPERWISE_API_VERSION}
      - SUPERWISE_APP_ID=${SUPERWISE_APP_ID}
      - API_TIMEOUT=${API_TIMEOUT:-30}
      - MAX_RETRIES=${MAX_RETRIES:-3}
      - RETRY_DELAY=${RETRY_DELAY:-1}
      - MAX_FILE_SIZE_MB=${MAX_FILE_SIZE_MB:-10}
      - APP_ENV=${APP_ENV:-development}
      - DEBUG=${DEBUG:-True}
      - LOG_LEVEL=${LOG_LEVEL:-INFO}
    volumes:
      - ./app:/app/app
      - ./logs:/app/logs
      - ./requirements.txt:/app/requirements.txt
    restart: unless-stopped
    healthcheck:
      test: ["CMD", "curl", "-f", "http://localhost:9000/_stcore/health"]
      interval: 30s
      timeout: 10s
      retries: 3
      start_period: 40s
```

### Dockerfile Features

- **Multi-stage build** for optimized production image
- **Python 3.11-slim** base image for security and size
- **Non-root user** for enhanced security
- **Health checks** for container monitoring
- **Hot reloading** enabled for development

## Environment Variables

### Required Variables
```bash
# Superwise API Configuration (Optional for demo)
SUPERWISE_API_URL=https://api.superwise.ai/
SUPERWISE_API_VERSION=v1
SUPERWISE_APP_ID=your_app_id_here
```

### Optional Variables
```bash
# API Settings
API_TIMEOUT=60
MAX_RETRIES=3
RETRY_DELAY=1

# File Upload Settings
MAX_FILE_SIZE_MB=10

# Application Settings
APP_ENV=development
DEBUG=true
LOG_LEVEL=INFO
```

## Volume Mounts

The Docker setup includes the following volume mounts for development:

- **`./app:/app/app`** - Application code (hot reloading)
- **`./logs:/app/logs`** - Application logs
- **`./requirements.txt:/app/requirements.txt`** - Dependency detection

## Common Docker Commands

### Development Commands
```bash
# Start the application
docker-compose up --build

# Start in background
docker-compose up --build -d

# View logs
docker-compose logs -f

# Stop the application
docker-compose down

# Rebuild without cache
docker-compose build --no-cache
```

### Container Management
```bash
# List running containers
docker ps

# Execute commands in running container
docker-compose exec legal-analyzer bash

# View container logs
docker-compose logs legal-analyzer

# Restart service
docker-compose restart legal-analyzer
```

### Cleanup Commands
```bash
# Stop and remove containers
docker-compose down

# Remove containers, networks, and volumes
docker-compose down -v

# Remove unused Docker resources
docker system prune
```

## Health Monitoring

The application includes built-in health checks:

- **Health Check Endpoint**: `/_stcore/health`
- **Check Interval**: 30 seconds
- **Timeout**: 10 seconds
- **Retries**: 3 attempts
- **Start Period**: 40 seconds

### Monitoring Health Status
```bash
# Check container health
docker ps

# View health check logs
docker-compose logs legal-analyzer | grep health

# Manual health check
curl -f http://localhost:9000/_stcore/health
```

## Troubleshooting

### Common Issues

#### Port Already in Use
```bash
# Check what's using port 9000
netstat -tulpn | grep 9000

# Change port in docker-compose.yml
ports:
  - "9001:9000"  # Use port 9001 instead
```

#### Environment Variables Not Loading
```bash
# Verify .env file exists
ls -la .env

# Check environment variables in container
docker-compose exec legal-analyzer env | grep SUPERWISE
```

#### Build Failures
```bash
# Clean build
docker-compose build --no-cache

# Check build logs
docker-compose build --progress=plain
```

#### Application Not Starting
```bash
# Check container logs
docker-compose logs legal-analyzer

# Check container status
docker-compose ps

# Restart with fresh build
docker-compose down && docker-compose up --build
```

### Log Analysis
```bash
# View real-time logs
docker-compose logs -f legal-analyzer

# View last 100 lines
docker-compose logs --tail=100 legal-analyzer

# View logs from specific time
docker-compose logs --since="2024-01-01T00:00:00" legal-analyzer
```

## Production Deployment

### Production Considerations

1. **Environment Variables**: Use secure secret management
2. **SSL/TLS**: Configure reverse proxy (nginx, traefik)
3. **Monitoring**: Set up container monitoring and alerting
4. **Backup**: Implement log and data backup strategies
5. **Scaling**: Use Docker Swarm or Kubernetes for scaling

### Production Docker Compose
```yaml
version: '3.8'
services:
  legal-analyzer:
    build: .
    ports:
      - "9000:9000"
    environment:
      - APP_ENV=production
      - DEBUG=false
      - LOG_LEVEL=WARNING
    restart: always
    healthcheck:
      test: ["CMD", "curl", "-f", "http://localhost:9000/_stcore/health"]
      interval: 30s
      timeout: 10s
      retries: 3
      start_period: 40s
```

## Security Best Practices

- **Non-root user**: Container runs as `streamlit` user
- **Minimal base image**: Uses `python:3.11-slim`
- **No unnecessary packages**: Only required dependencies installed
- **Health checks**: Regular container health monitoring
- **Environment variables**: Sensitive data via environment variables
- **Volume mounts**: Only necessary directories mounted

## Support

For Docker-related issues:

1. Check the troubleshooting section above
2. Review container logs: `docker-compose logs legal-analyzer`
3. Verify environment configuration
4. Ensure Docker Desktop is running properly

## Additional Resources

- [Docker Documentation](https://docs.docker.com/)
- [Docker Compose Documentation](https://docs.docker.com/compose/)
- [Streamlit Docker Guide](https://docs.streamlit.io/knowledge-base/tutorials/docker)

