#!/usr/bin/env python3
import time
import os

def display_stats():
    load1, load5, load15 = os.getloadavg() if hasattr(os, "getloadavg") else (0, 0, 0)
    print(f"System Load: {load1:.2f}, {load5:.2f}, {load15:.2f}")

if __name__ == '__main__':
    display_stats()
