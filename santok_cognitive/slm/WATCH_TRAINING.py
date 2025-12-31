"""
Watch Training Progress
=======================

Monitor the training progress and notify when model is ready.
"""

import os
import sys
import time

print("\n" + "=" * 70)
print("Watching Training Progress")
print("=" * 70)
print()

model_path = os.path.join(os.path.dirname(__file__), "santok_lgm_trained_on_santok.pkl")
log_path = os.path.join(os.path.dirname(__file__), "training_output.log")

print(f"Model will be saved to: {os.path.abspath(model_path)}")
print(f"Training log: {os.path.abspath(log_path)}")
print()
print("Checking for model every 10 seconds...")
print("Press Ctrl+C to stop watching")
print()

check_count = 0
while True:
    check_count += 1
    
    if os.path.exists(model_path):
        size_mb = os.path.getsize(model_path) / (1024 * 1024)
        print()
        print("=" * 70)
        print("[OK] MODEL IS READY!")
        print("=" * 70)
        print()
        print(f"Model file: {os.path.abspath(model_path)}")
        print(f"Size: {size_mb:.2f} MB")
        print()
        print("You can now load it with:")
        print("  python FIND_AND_LOAD_MODEL.py")
        print("  python GET_MODEL.py")
        print()
        break
    
    # Show progress
    if check_count % 6 == 0:  # Every minute
        print(f"[{check_count * 10}s] Still training... (checking every 10 seconds)")
    
    # Check log file for progress
    if os.path.exists(log_path):
        try:
            with open(log_path, 'r', encoding='utf-8', errors='ignore') as f:
                lines = f.readlines()
                if lines:
                    # Show last few lines
                    last_lines = [l.strip() for l in lines[-3:] if l.strip()]
                    if last_lines:
                        print(f"  Latest: {last_lines[-1][:80]}")
        except:
            pass
    
    time.sleep(10)
