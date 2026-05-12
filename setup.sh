#!/bin/bash

echo "=== Prashant Bathula Resume Website Setup ==="
echo

# Check if git is installed
if ! command -v git &> /dev/null; then
    echo "❌ Git is not installed. Please install git first."
    echo "   Ubuntu/Debian: sudo apt-get install git"
    echo "   macOS: brew install git"
    echo "   Windows: Download from https://git-scm.com/"
    exit 1
fi

# Check if GitHub CLI is installed (optional but helpful)
if ! command -v gh &> /dev/null; then
    echo "ℹ️  GitHub CLI (gh) is not installed. You can still use this setup with regular git commands."
    echo "   Install gh from: https://github.com/cli/cli"
    echo
fi

echo "✅ Git is installed"
echo

# Check if we're in a git repository
if [ ! -d ".git" ]; then
    echo "🚀 Initializing git repository..."
    git init
    echo "✅ Git repository initialized"
else
    echo "✅ Git repository already exists"
fi

echo

# Check if index.html exists
if [ ! -f "index.html" ]; then
    echo "❌ index.html not found. Please make sure the resume file is in the current directory."
    exit 1
fi

echo "✅ index.html found"
echo

# Check if README.md exists
if [ ! -f "README.md" ]; then
    echo "❌ README.md not found. Please make sure the README file is in the current directory."
    exit 1
fi

echo "✅ README.md found"
echo

# Create .gitignore file
echo "📝 Creating .gitignore file..."
cat > .gitignore << EOF
# Python
__pycache__/
*.py[cod]
*$py.class
*.so
.Python
build/
develop-eggs/
dist/
downloads/
eggs/
.eggs/
lib/
lib64/
parts/
sdist/
var/
wheels/
*.egg-info/
.installed.cfg
*.egg

# PDF generation files
resume.pdf.txt
*.log

# IDE
.vscode/
.idea/
*.swp
*.swo

# OS
.DS_Store
Thumbs.db

# Temporary files
*.tmp
*.temp
EOF

echo "✅ .gitignore created"
echo

# Add files to git
echo "📦 Adding files to git repository..."
git add .
echo "✅ Files added to git"
echo

# Initial commit
echo "📝 Creating initial commit..."
git commit -m "Initial commit: Resume website for Prashant Bathula"
echo "✅ Initial commit created"
echo

echo "=== Setup Complete! ==="
echo
echo "Next steps:"
echo "1. Create a new repository on GitHub:"
echo "   - Go to https://github.com/"
echo "   - Click '+' → 'New repository'"
echo "   - Name it: 'prashantbat.github.io'"
echo "   - Make it public"
echo "   - Don't initialize with README (we already have one)"
echo "   - Click 'Create repository'"
echo
echo "2. Link your local repository to GitHub:"
echo "   git remote add origin https://github.com/prashantbat/prashantbat.github.io.git"
echo
echo "3. Push your files to GitHub:"
echo "   git push -u origin main"
echo
echo "4. Enable GitHub Pages:"
echo "   - Go to your repository on GitHub"
echo "   - Click 'Settings'"
echo "   - Click 'Pages' in the left sidebar"
echo "   - Under 'Source', select 'Deploy from a branch'"
echo "   - Branch: 'main'"
echo "   - Folder: '/ (root)'"
echo "   - Click 'Save'"
echo
echo "5. Create your PDF:"
echo "   - Open index.html in your web browser"
echo "   - Press Ctrl+P (or Cmd+P on Mac)"
echo "   - Select 'Save as PDF'"
echo "   - Save as 'resume.pdf'"
echo "   - Add and commit the PDF file:"
echo "     git add resume.pdf"
echo "     git commit -m 'Add PDF version of resume'"
echo "     git push origin main"
echo
echo "6. Your resume will be live at:"
echo "   https://prashantbat.github.io"
echo
echo "🎉 Congratulations! Your resume website is ready!"