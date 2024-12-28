# Define the paths to the Vue project and backend project
$frontendPath = "frontend"
$backendPath = "backend"

# Define the commands to run Vue script and activate virtual environment
$vueCommand = "pnpm run dev"
$activateVenvCommand = "& venv\Scripts\Activate"
$pythonCommand = "py .\src\main.py"

# Create a new process for running the Vue script
$vueProcessInfo = New-Object System.Diagnostics.ProcessStartInfo
$vueProcessInfo.FileName = "powershell.exe"
$vueProcessInfo.Arguments = "/c $vueCommand"
$vueProcessInfo.WorkingDirectory = $frontendPath
$vueProcessInfo.WindowStyle = "Normal"  # You can set this to "Hidden" if you don't want the window to be visible
$vueProcess = [System.Diagnostics.Process]::Start($vueProcessInfo)

# Create a new process for activating the virtual environment and running Python script
$activateVenvProcessInfo = New-Object System.Diagnostics.ProcessStartInfo
$activateVenvProcessInfo.FileName = "powershell.exe"
$activateVenvProcessInfo.Arguments = "/c $activateVenvCommand ; $pythonCommand ; pause"
$activateVenvProcessInfo.WorkingDirectory = $backendPath
$activateVenvProcessInfo.WindowStyle = "Normal"  # You can set this to "Hidden" if you don't want the window to be visible
$activateVenvProcess = [System.Diagnostics.Process]::Start($activateVenvProcessInfo)
