#!/usr/bin/env python3
import subprocess
import sys
import os

def install_puppeteer():
    """Install Puppeteer for PDF generation"""
    try:
        print("Installing Puppeteer...")
        subprocess.run([sys.executable, "-m", "pip", "install", "puppeteer"], check=True)
        print("Puppeteer installed successfully!")
        return True
    except subprocess.CalledProcessError:
        print("Failed to install Puppeteer. Trying alternative method...")
        return False

def create_pdf_with_puppeteer():
    """Create PDF using Puppeteer"""
    try:
        import asyncio
        import base64
        from io import BytesIO
        
        async def generate_pdf():
            import pyppeteer
            
            browser = await pyppeteer.launch()
            page = await browser.newPage()
            
            # Read HTML file
            with open('index.html', 'r', encoding='utf-8') as f:
                html_content = f.read()
            
            await page.setContent(html_content, waitUntil='networkidle0')
            
            # Generate PDF
            pdf = await page.pdf({
                'format': 'A4',
                'printBackground': True,
                'margin': {
                    'top': '0.5cm',
                    'bottom': '0.5cm',
                    'left': '0.5cm',
                    'right': '0.5cm'
                }
            })
            
            await browser.close()
            return pdf
        
        # Run the async function
        pdf_content = asyncio.run(generate_pdf())
        
        # Save PDF
        pdf_filename = "PrashantBathula.pdf"
        with open(pdf_filename, 'wb') as f:
            f.write(pdf_content)
        
        print(f"PDF created successfully: {pdf_filename}")
        return True
        
    except ImportError:
        print("Pyppeteer not installed. Installing...")
        if install_puppeteer():
            return create_pdf_with_puppeteer()
        else:
            return False
    except Exception as e:
        print(f"Error creating PDF with Puppeteer: {e}")
        return False

def create_pdf_with_weasyprint():
    """Create PDF using WeasyPrint (alternative method)"""
    try:
        import weasyprint
        
        print("Creating PDF with WeasyPrint...")
        
        # Read HTML file
        with open('index.html', 'r', encoding='utf-8') as f:
            html_content = f.read()
        
        # Create PDF
        pdf_filename = "PrashantBathula.pdf"
        weasyprint.HTML(string=html_content, base_url='.').write_pdf(pdf_filename)
        
        print(f"PDF created successfully: {pdf_filename}")
        return True
        
    except ImportError:
        print("WeasyPrint not installed. Installing...")
        try:
            subprocess.run([sys.executable, "-m", "pip", "install", "weasyprint"], check=True)
            return create_pdf_with_weasyprint()
        except subprocess.CalledProcessError:
            return False
    except Exception as e:
        print(f"Error creating PDF with WeasyPrint: {e}")
        return False

def create_simple_pdf():
    """Create a simple text-based PDF as fallback"""
    try:
        from reportlab.pdfgen import canvas
        from reportlab.lib.pagesizes import letter
        from reportlab.lib.units import inch
        
        print("Creating simple text-based PDF...")
        
        pdf_filename = "PrashantBathula.pdf"
        c = canvas.Canvas(pdf_filename, pagesize=letter)
        
        # Title
        c.setFont("Helvetica-Bold", 24)
        c.drawString(inch, 10.5*inch, "Prashant Bathula")
        c.setFont("Helvetica", 16)
        c.drawString(inch, 10*inch, "DevOps SRE & Technical Architect")
        
        # Contact info
        c.setFont("Helvetica", 12)
        c.drawString(inch, 9.5*inch, "Email: prashantbathula1993@gmail.com")
        c.drawString(inch, 9.2*inch, "Phone: +91 9867032410")
        c.drawString(inch, 8.9*inch, "LinkedIn: https://www.linkedin.com/in/prashant-bathula")
        
        # Experience summary
        c.setFont("Helvetica-Bold", 14)
        c.drawString(inch, 8.3*inch, "Experience Summary")
        c.setFont("Helvetica", 11)
        
        text = """
10+ years of IT experience in Advanced DevOps technologies, Kubernetes, Openshift Admin, 
Various cloud technologies. Designed and maintained CI/CD pipelines using GitLab to 
automate build, test, and deployment processes for enterprise applications. Implemented 
Infrastructure as Code (IaC) using Terraform to provision and manage cloud infrastructure 
environments, ensuring consistent and repeatable deployments.
        """.strip()
        
        # Simple text wrapping (basic implementation)
        lines = []
        words = text.split()
        current_line = ""
        
        for word in words:
            test_line = current_line + word + " "
            if c.stringWidth(test_line, "Helvetica", 11) < 7.5*inch:
                current_line = test_line
            else:
                if current_line:
                    lines.append(current_line.strip())
                current_line = word + " "
        
        if current_line:
            lines.append(current_line.strip())
        
        y_position = 8.0*inch
        for line in lines:
            if y_position > 0.5*inch:
                c.drawString(inch, y_position, line)
                y_position -= 0.3*inch
            else:
                # New page if we run out of space
                c.showPage()
                y_position = 10.5*inch
        
        c.save()
        print(f"Simple PDF created successfully: {pdf_filename}")
        return True
        
    except ImportError:
        print("ReportLab not installed. Installing...")
        try:
            subprocess.run([sys.executable, "-m", "pip", "install", "reportlab"], check=True)
            return create_simple_pdf()
        except subprocess.CalledProcessError:
            return False
    except Exception as e:
        print(f"Error creating simple PDF: {e}")
        return False

def main():
    print("Resume PDF Generator")
    print("=" * 30)
    
    # Try different methods in order of preference
    methods = [
        ("Puppeteer (recommended)", create_pdf_with_puppeteer),
        ("WeasyPrint", create_pdf_with_weasyprint),
        ("ReportLab (simple)", create_simple_pdf)
    ]
    
    for method_name, method_func in methods:
        print(f"\nTrying {method_name}...")
        if method_func():
            print(f"✅ Success! PDF generated using {method_name}")
            break
    else:
        print("❌ Failed to generate PDF with any method")
        print("\nManual instructions:")
        print("1. Open index.html in a web browser")
        print("2. Press Ctrl+P (or Cmd+P on Mac)")
        print("3. Choose 'Save as PDF' as the printer")
        print("4. Save as resume.pdf")
        return False
    
    return True

if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)