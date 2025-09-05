# scripts/generate_transcript_stub.py
# Simple helper that creates a small transcript file for testing.
import sys
out = """
[00:00] Host: Welcome to episode 12...
[02:10] Guest: We scaled by focusing on...
[10:30] Host: Final thoughts...
"""
path = sys.argv[1] if len(sys.argv)>1 else 'demo_transcript.txt'
with open(path,'w') as f:
    f.write(out)
print('Wrote', path)
