# Resume Website Setup Instructions

## Quick Start

### 1. Clone Your Repository
```bash
git clone https://github.com/prashantbat/resume.git
cd resume
```

### 2. Open Resume in Browser
```bash
# Open the resume HTML file
open index.html
# Or use:
# xdg-open index.html   # Linux
# start index.html      # Windows
```

### 3. Create PDF Version
Open `index.html` in your web browser:
1. Press Ctrl+P (or Cmd+P on Mac)
2. Select "Save as PDF" as the destination printer
3. Click "Save" and name the file "resume.pdf"
4. Make sure to save it in the same directory as index.html

### 4. Add PDF to Repository
```bash
git add resume.pdf
git commit -m "Add PDF version of resume"
git push origin main
```

## Manual GitHub Setup

If you prefer to do it manually:

### 1. Go to Your Repository
Visit: https://github.com/prashantbat/resume

### 2. Upload Files
- Click "Add file" → "Upload files"
- Drag and drop or select these files:
  - `index.html`
  - `README.md`
  - `resume.pdf` (after creating it)
  - `.gitignore`

### 3. Enable GitHub Pages
1. Click "Settings"
2. Click "Pages" in the left sidebar
3. Under "Source", select "Deploy from a branch"
4. Branch: "main"
5. Folder: "/ (root)"
6. Click "Save"

## GitHub Pages Activation

After pushing your files:
1. Go to your repository on GitHub
2. Navigate to Settings → Pages
3. The deployment should start automatically
4. Your resume will be live at: https://prashantbat.github.io/resume

## Customization Tips

### Update Contact Information
Edit the contact section in `index.html`:
```html
<div class="contact-info">
    <div class="contact-item">📱 +91 9867032410</div>
    <div class="contact-item">✉️ prashantbathula1993@gmail.com</div>
    <div class="contact-item">💼 https://www.linkedin.com/in/prashant-bathula</div>
</div>
```

### Update Experience
Edit the experience sections in `index.html` to reflect your current role and achievements.

### Update Skills
Modify the skills grid in the "Technical Skills" section.

## Troubleshooting

### GitHub Pages Not Loading
- Wait 5-10 minutes for deployment to complete
- Ensure repository is set to public
- Check that Pages is enabled in settings

### PDF Download Not Working
- Make sure `resume.pdf` is in the root directory
- Ensure the file is added and committed to the repository

### Design Issues
- The website is responsive and should work on all modern browsers
- Test on different devices to ensure proper display

## Support

For any issues or questions:
- Check the GitHub Pages documentation
- Review the GitHub repository settings
- Feel free to reach out for professional inquiries

---

Good luck with your job search! 🚀