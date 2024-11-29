import os
import shutil
import git
from git.exc import GitCommandError

def copy_specific_directory(repo_url, local_dir, target_subdir):
    """
    Clone a specific directory from a GitHub repository.
    This script clones the whole repository, then extracts the specified directory.
    """
    try:
        # Step 1: Clone the repository (shallow clone for performance)
        print(f"Cloning repository from '{repo_url}' into '{local_dir}'...")
        temp_repo_dir = os.path.join(local_dir, "temp_repo")  # Temporary directory for the repository
        if os.path.exists(temp_repo_dir):
            shutil.rmtree(temp_repo_dir)
        git.Repo.clone_from(repo_url, temp_repo_dir, depth=1)
        print("Repository cloned successfully.")

        # Step 2: Locate and copy the target directory
        source_dir = os.path.join(temp_repo_dir, target_subdir)
        if not os.path.exists(source_dir):
            print(f"Error: Target directory '{target_subdir}' not found in the repository.")
            shutil.rmtree(temp_repo_dir)
            return
        
        destination_dir = os.path.join(local_dir, target_subdir)
        if os.path.exists(destination_dir):
            shutil.rmtree(destination_dir)  # Clean up existing target directory
        shutil.copytree(source_dir, destination_dir)
        print(f"Copied '{target_subdir}' to '{destination_dir}'.")

        # Step 3: Clean up the temporary repository
        shutil.rmtree(temp_repo_dir)
        print("Temporary repository cleaned up.")

    except GitCommandError as e:
        print(f"Error cloning repository: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    # Replace these with your repository URL and local directory
    repo_url = "https://github.com/nadeeshafdo/HandyCLI.git"  # GitHub repository URL
    local_dir = "./local_copy"  # Local directory to copy the target subdir
    target_subdir = "$"  # Subdirectory to copy

    copy_specific_directory(repo_url, local_dir, target_subdir)
