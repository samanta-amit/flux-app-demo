import docker
import time
import sys

def get_pull_time(image_name):
    """
    Pulls a Docker image and returns the time it took in seconds.
    This function first removes the image to ensure a fresh pull.
    """
    client = docker.from_env()
    pull_start_time = None
    pull_end_time = None
    
    # Try to remove the image first to get an accurate pull time
    try:
        print(f"Removing existing image: {image_name}...")
        client.images.remove(image_name, force=True)
        print("Image removed successfully.")
    except docker.errors.ImageNotFound:
        print(f"Image {image_name} not found locally. Proceeding with pull.")
    except Exception as e:
        print(f"Could not remove image {image_name}: {e}. Proceeding with pull anyway.")

    print(f"Pulling image: {image_name}...")
    
    try:
        pull_start_time = time.time()
        # The pull() method returns an iterator that streams the pull process
        for line in client.api.pull(image_name, stream=True, decode=True):
            # We just iterate through the stream to ensure the pull completes
            # You can add logic here to print progress if you want
            pass
        pull_end_time = time.time()
        
        # Check if the pull was successful
        try:
            client.images.get(image_name)
            pull_duration = pull_end_time - pull_start_time
            return pull_duration
        except docker.errors.ImageNotFound:
            print(f"Error: Image {image_name} was not pulled successfully.")
            return None

    except Exception as e:
        print(f"An error occurred while pulling image {image_name}: {e}")
        return None

if __name__ == "__main__":
    apps = {
        "amg2023": "ghcr.io/converged-computing/metric-amg2023:spack-slim-cpu-int64-zen3",
        "kripke": "ghcr.io/converged-computing/metric-kripke-cpu:libfabric-zen4",
        "lammps-reax": "ghcr.io/converged-computing/metric-lammps-cpu:libfabric-zen4-reax",
        "minife": "ghcr.io/converged-computing/metric-minife:libfabric-cpu-zen4",
        "mt-gemm": "ghcr.io/converged-computing/mt-gemm:libfabric-cpu-zen4-1k",
        "quicksilver": "ghcr.io/converged-computing/metric-quicksilver-cpu:libfabric-zen4"
    }

    pull_times = {}

    for app_name, image_url in apps.items():
        pull_time = get_pull_time(image_url)
        if pull_time is not None:
            pull_times[app_name] = pull_time
        print("-" * 30)

    print("\n--- Docker Image Pull Times ---")
    for app, pull_time in pull_times.items():
        print(f"{app:<15}: {pull_time:.2f} seconds")
