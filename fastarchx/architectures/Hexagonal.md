# Hexagonal Architecture (Ports & Adapters) with FastAPI

## Overview
Core domain is isolated; everything else is an adapter.

## FastAPI Role
API is an adapter.

## Core idea
Domain exposes ports, adapters implement them.

## Structure
- core/domain
- core/ports
- adapters/api
- adapters/db

## When to use
Systems needing flexibility in infrastructure.
