import yaml
import pprint

def load_config():
    with open("config.yaml", "r") as conf_file:
        return yaml.safe_load(conf_file)

def main():
    config = load_config()
    
    print(f"\nconfig: {pprint.pformat(config['scraper']['content'])}")
    # success: can access nested contents and yaml is correctly formatted

if __name__ == "__main__":
    main()
