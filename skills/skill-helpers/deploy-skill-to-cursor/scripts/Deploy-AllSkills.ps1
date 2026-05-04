<#
.SYNOPSIS
  Junction ~/.cursor/skills directly to the repo's skills/ folder.
#>
param(
    [string] $SkillsRepoRoot = "",
    [string] $CursorSkillsRoot = $(Join-Path $env:USERPROFILE '.cursor\skills'),
    [switch] $Force
)

$ErrorActionPreference = 'Stop'

if (-not $SkillsRepoRoot) {
    $SkillsRepoRoot = Resolve-Path (Join-Path $PSScriptRoot '..\..\..') |
                      Select-Object -ExpandProperty Path
}

$source = Join-Path $SkillsRepoRoot 'skills'

if (Test-Path -LiteralPath $CursorSkillsRoot) {
    if (-not $Force) {
        Write-Host "EXISTS (use -Force to replace): $CursorSkillsRoot" -ForegroundColor Yellow
        exit 0
    }
    Remove-Item -LiteralPath $CursorSkillsRoot -Recurse -Force
}

New-Item -ItemType Junction -Path $CursorSkillsRoot -Target $source | Out-Null
Write-Host "OK: $CursorSkillsRoot -> $source" -ForegroundColor Green
