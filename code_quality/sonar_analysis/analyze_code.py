import os
import subprocess

SONARQUBE_HOST = ""
PROJECT_KEY = ""
SONAR_TOKEN = ""

def run_sonar_analysis():
    # Define the sonar-scanner command
    sonar_command = [
        "sonar-scanner",
        f"-Dsonar.projectKey={PROJECT_KEY}",
        f"-Dsonar.sources=.",
        f"-Dsonar.host.url={SONARQUBE_HOST}",
        f"-Dsonar.login={SONAR_TOKEN}"
    ]

    # Run the sonar-scanner command
    try:
        result = subprocess.run(sonar_command, check=True, text=True, capture_output=True)
        print("SonarQube analysis completed successfully.")
        print(result.stdout)
    except subprocess.CalledProcessError as e:
        print("SonarQube analysis failed.")
        print(e.output)

if __name__ == "__main__":
    run_sonar_analysis()
