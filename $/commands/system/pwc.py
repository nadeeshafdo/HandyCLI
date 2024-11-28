import os
import sys
import argparse
from impacket.examples.secretsdump import LocalOperations, NTDSHashes
import impacket.winregistry

def extract_ntlm_hashes(sam_hive_path, system_hive_path, output_file):
    try:
        # Load SYSTEM hive and get boot key
        system_hive = Registry(system_hive_path)
        bootkey = LocalOperations(system_hive_path).getBootKey()

        # Load SAM hive using boot key
        sam_hive = Registry(sam_hive_path, bootkey=bootkey)
        sam_hashes = NTDSHashes(None, bootkey, isRemote=False, useVSSMethod=False, samFile=sam_hive)

        # Dump and export NTLM hashes
        sam_hashes.dump()
        sam_hashes.export(output_file)
        sam_hashes.finish()
        print(f"NTLM hashes extracted successfully and saved to {output_file}.")
    except Exception as e:
        print(f"Failed to extract NTLM hashes: {e}")

def main():
    parser = argparse.ArgumentParser(description="Extract NTLM hashes from SAM and SYSTEM files.")
    parser.add_argument("sam", help="Path to the SAM file.")
    parser.add_argument("system", help="Path to the SYSTEM file.")
    parser.add_argument("-o", "--output", default="hashes.txt", help="Output file for the NTLM hashes (default: hashes.txt).")
    
    args = parser.parse_args()
    
    sam_hive_path = args.sam
    system_hive_path = args.system
    output_file = args.output
    
    if not os.path.exists(sam_hive_path):
        print(f"Error: SAM file '{sam_hive_path}' does not exist.")
        sys.exit(1)
        
    if not os.path.exists(system_hive_path):
        print(f"Error: SYSTEM file '{system_hive_path}' does not exist.")
        sys.exit(1)
    
    print("Extracting NTLM hashes...")
    extract_ntlm_hashes(sam_hive_path, system_hive_path, output_file)

if __name__ == "__main__":
    main()
