echo [$(date)]: "START"
echo [$(date)]: "Creating conda env"
conda create --prefix ./env python=3.8 -y
echo [$(date)]: "activate env"
source activte ./env
echo [$(date)]: "installing dev requirements"
pip install -r requirements_dev.txt
echo [$(date)]: "END"