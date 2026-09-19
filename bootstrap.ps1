$ErrorActionPreference = "Stop"

# Thin remote launcher. All target inspection and writes stay in .agent/bootstrap.py.
$AosRepoUrl = if ($env:AOS_REPO_URL) {
    $env:AOS_REPO_URL
} else {
    "https://github.com/Nezarabdluah/My-Programming-Workflow.git"
}
$AosRef = if ($env:AOS_REF) { $env:AOS_REF } else { "main" }
$AosTarget = if ($env:AOS_TARGET) {
    (Resolve-Path -LiteralPath $env:AOS_TARGET).Path
} else {
    (Get-Location).Path
}
$AosTempDir = Join-Path ([System.IO.Path]::GetTempPath()) (
    "aos-bootstrap-" + [System.Guid]::NewGuid().ToString("N")
)

if (-not (Get-Command git -ErrorAction SilentlyContinue)) {
    throw "AOS BOOTSTRAP BLOCKED: git is required."
}

$PythonCommand = if (Get-Command py -ErrorAction SilentlyContinue) {
    $PythonArguments = @("-3")
    "py"
} elseif (Get-Command python3 -ErrorAction SilentlyContinue) {
    $PythonArguments = @()
    "python3"
} elseif (Get-Command python -ErrorAction SilentlyContinue) {
    $PythonArguments = @()
    "python"
} else {
    throw "AOS BOOTSTRAP BLOCKED: Python 3 is required."
}

try {
    New-Item -ItemType Directory -Path $AosTempDir -Force | Out-Null
    & git -C $AosTempDir init -q
    if ($LASTEXITCODE -ne 0) { throw "AOS source initialization failed." }
    & git -C $AosTempDir remote add origin $AosRepoUrl
    if ($LASTEXITCODE -ne 0) { throw "AOS source remote setup failed." }
    & git -C $AosTempDir fetch -q --depth 1 origin $AosRef
    if ($LASTEXITCODE -ne 0) { throw "AOS source download failed for ref '$AosRef'." }
    & git -C $AosTempDir checkout -q --detach FETCH_HEAD
    if ($LASTEXITCODE -ne 0) { throw "AOS source checkout failed." }

    $Bootstrap = Join-Path $AosTempDir ".agent/bootstrap.py"
    & $PythonCommand @PythonArguments $Bootstrap $AosTarget
    if ($LASTEXITCODE -ne 0) {
        throw "AOS bootstrap stopped with exit code $LASTEXITCODE."
    }
} finally {
    if (Test-Path -LiteralPath $AosTempDir) {
        Remove-Item -LiteralPath $AosTempDir -Recurse -Force
    }
}
