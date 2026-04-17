from pathlib import Path
import os

def fix_settings():
    path = Path('sky_registry/settings.py')
    content = path.read_text()
    
    # 1. Update imports and load_dotenv
    if "from dotenv import load_dotenv" not in content:
        import_block = "import os\nfrom pathlib import Path\nfrom dotenv import load_dotenv\n\n# Load environment variables from .env file\nload_dotenv(os.path.join(Path(__file__).resolve().parent.parent, '.env'))\n"
        content = content.replace("from pathlib import Path", import_block)
    
    # 2. Update SECRET_KEY
    old_sk = "SECRET_KEY = 'django-insecure-s9@amep!%ci3e^3f2=4*2=m^w!aym^qok19u%9!-=u)9m_q_nx'"
    new_sk = "SECRET_KEY = os.getenv('SECRET_KEY', 'django-insecure-s9@amep!%ci3e^3f2=4*2=m^w!aym^qok19u%9!-=u)9m_q_nx')"
    content = content.replace(old_sk, new_sk)
    
    # 3. Update DEBUG
    content = content.replace("DEBUG = True", "DEBUG = os.getenv('DEBUG', 'True') == 'True'")
    
    path.write_text(content)
    print("Settings updated successfully.")

if __name__ == "__main__":
    fix_settings()
