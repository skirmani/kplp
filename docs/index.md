# kplp Documentation

## Overview

Kirmani Partners LP pitchbook (GitHub Pages)

## Architecture

This module is part of the Kirmani Partners LP quantitative trading ecosystem.
It communicates via the Kirmani Signal Protocol (KSP) and integrates with the
Kirmani Decision Engine (KDE) pipeline.

## API Reference

See source code docstrings for detailed API documentation.

## Configuration

Configuration is managed via YAML files in the `configs/` directory
and environment variables.

## Deployment

```bash
docker build -t kplp .
docker run -e ENV=production kplp
```
