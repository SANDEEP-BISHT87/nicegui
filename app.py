from nicegui import ui

# Main website styling with a gradient background
with ui.row().style('background: linear-gradient(to bottom, #B7E7FE, #ffffff); padding: 2px 2px;'):

    

    # Company Icon and Title
    with ui.column().style('align-items: center; margin: 32px; text-align: center;'):
        # Row to contain the image and title
        with ui.row().style('align-items: center; justify-content: center;'):
            # Adding the company logo (image) next to the title
            ui.image('./public/image/ntools.png').style('width: 80px; height: 80px; margin-right: 16px;')  # Company logo image
            
            # Title and subtitle labels
            ui.label('NIBBLE TOOLS RECOVERY ').classes('text-5xl font-extrabold mb-4 text-gray-900')
        
        ui.label('Data recovery made easy for HDD, SSD,VHD RAID, and more').classes('text-lg text-gray-600')

    # Create a container for the 3D rotating effect
    # Link the external CSS file
    ui.add_css('./public/static/app.css')
    # Assuming app.css is correctly linked in your project, with 3D rotation styles.
    with ui.element('div').classes('card-container'):
        with ui.element('div').classes('card-carousel'):
            for i in range(5):
                with ui.element('div').classes('card').style('--position: {}; --quantity: 5;'.format(i + 1)):
                    ui.image(f'./public/image/card-{i+1}.jpg').style('width: 100%; height: 100%; object-fit: cover; border-radius: 10px;')



            
        

    # Header Section
    with ui.column().style('text-align: center; margin-bottom: 48px;'):
        ui.label('Recover Lost, Deleted, Formatted, Corrupt Files Completely & Easily').classes('text-3xl font-semibold mb-4 text-gray-800')
        ui.label('Recover 1000+ File Types').classes('text-xl mb-2 text-gray-600')

    # Features List Section
    with ui.column().style('padding: 16px; margin-bottom: 40px;'):
        features = [
            '√ We Support Nearly All Hard Drives You Use.',
            '√ Support 1000+ File Formats: Office Documents, Photos, Videos, etc.',
            '√ Support Different Data Loss Situations: Crash, Physical Damage, Deleted, Formatted, etc.'
        ]
        for feature in features:
            ui.label(feature).classes('text-md mb-4 text-gray-700')

# Categories Section with Colorful but Professional Cards
categories = {
    "Photos/Pictures": "JPG/JPEG, TIFF/TIF, PNG, BMP, GIF, PSD, CRW, CR2, NEF, ORF, SR2, MRW, DCR, WMF, RAW, SWF, SVG, RAF, DNG, ERF, ICO, DSC, etc.",
    "Videos": "AVI, MOV, MP4, M4V, 3GP, 3G2, WMV, MKV, ASF, FLV, F4V, SWF, MPG, RM/RMVB, MPEG, TS, VOB, MTS, DV, etc.",
    "Music/Audios": "MP3, AIF/AIFF, M4A, WMA, APE, MID/MIDI, VQF, OGG, AAC, WAV, FLAC, DTS and other audio formats.",
    "Office Documents": "DOC/DOCX, XLS/XLSX, PPT/PPTX, CWK, HTML/HTM, INDD, EPS, RTF, EPUB, CHM, CSV, TXT, DOTM, THMX, and so on.",
    "RAR/ZIP": "RAR, ZIP, 7Z, BZ2, ISO, IMG, TAR, GZ, TAZ, TGZ, LHA, LZH, CAB, TZ, Z, BZIP2, GZIP, WIM, AR, ARJ, DMG and so much more.",
    "Other Files": "Get back other possible files in different loss situations easily."
}

colors = [
    "#ffcccb",  # Light Red for Photos/Pictures
    "#ffeb3b",  # Yellow for Videos
    "#81c784",  # Green for Music/Audios
    "#64b5f6",  # Blue for Office Documents
    "#ff7043",  # Orange for RAR/ZIP
    "#ba68c8"   # Purple for Other Files
]

# Creating colorful but subtle professional cards for each category with animation
with ui.row().style('flex-wrap: wrap; justify-content: space-between; gap: 20px; margin-bottom: 40px;'):
    for i, (category, details) in enumerate(categories.items()):
        with ui.card().classes('p-6 shadow-lg max-w-xs hover:scale-105 transition-all duration-300 ease-in-out').style(
                f'background: {colors[i]}; border-radius: 12px; border: 1px solid rgba(0,0,0,0.1); position: relative;'):

            # Card text and content
            ui.label(category).classes('text-xl font-semibold mb-2 text-gray-900')
            ui.label(details).classes('text-sm text-gray-700')

            # Adding a subtle shadow effect when hovered
            with ui.card().classes('absolute inset-0 bg-black opacity-0 hover:opacity-10 transition-opacity duration-300 rounded-xl'):

                pass  # This will create an overlay with a slight shadow effect when hovered


# Restructured Card container for different services with elegant designs
with ui.row().classes('justify-around flex-wrap gap-6'):
    # HDD Recovery Card
    # Card with image hover effect for pop-out
    with ui.card().classes('shadow-xl rounded-xl overflow-hidden max-w-xs relative hover:scale-105 transition-transform duration-300').style('background: #1d3557; color: white;'):
        ui.image('./public/image/hdd.jpg').classes('w-full transition-transform duration-300 transform hover:scale-110')
        ui.label('HDD/SSD Recovery').classes('text-xl font-semibold mt-2 mb-2 text-center')
        ui.label('Advanced HDD data recovery software to rescue lost or corrupted data.').classes('text-sm mb-4 px-4')
        ui.button('Buy Now', on_click=lambda: ui.notify('Redirecting to HDD Recovery purchase page')).classes('bg-yellow-500 text-white mx-4 mb-4')


    # VIRTUAL DISK Recovery Card
    with ui.card().classes('shadow-xl rounded-xl overflow-hidden max-w-xs relative hover:scale-105 transition-transform duration-300').style('background: #e63946; color: white;'):
        ui.image('./public/image/virtual.jpg').classes('w-full transition-transform duration-300 transform hover:scale-110')
        ui.label('VIRTUAL DISK Recovery').classes('text-xl font-semibold mt-2 mb-2 text-center')
        ui.label('Reliable VIRTUAL DISK recovery software to retrieve important data.').classes('text-sm mb-4 px-4')
        ui.button('Buy Now', on_click=lambda: ui.notify('Redirecting to virtual disk  Recovery purchase page')).classes('bg-yellow-500 text-white mx-4 mb-4')

    # RAID Recovery Card
    with ui.card().classes('shadow-xl rounded-xl overflow-hidden max-w-xs relative hover:scale-105 transition-transform duration-300').style('background: #2a9d8f; color: white;'):
        ui.image('./public/image/raid.jpg').classes('w-full transition-transform duration-300 transform hover:scale-110')
        ui.label('RAID Recovery').classes('text-xl font-semibold mt-2 mb-2 text-center')
        ui.label('Comprehensive RAID recovery solutions for data recovery.').classes('text-sm mb-4 px-4')
        ui.button('Buy Now', on_click=lambda: ui.notify('Redirecting to RAID Recovery purchase page')).classes('bg-yellow-500 text-white mx-4 mb-4')

    # EWF Recovery Card
    with ui.card().classes('shadow-xl rounded-xl overflow-hidden max-w-xs relative hover:scale-105 transition-transform duration-300').style('background: #6a0572; color: white;'):
        ui.image('./public/image/ewf.jpg').classes('w-full transition-transform duration-300 transform hover:scale-110')
        ui.label('EWF Recovery').classes('text-xl font-semibold mt-2 mb-2 text-center')
        ui.label('Specialized software to recover files from EWF formats.').classes('text-sm mb-4 px-4')
        ui.button('Buy Now', on_click=lambda: ui.notify('Redirecting to EWF Recovery purchase page')).classes('bg-yellow-500 text-white mx-4 mb-4')

    # HDD IMAGE Card
    with ui.card().classes('shadow-xl rounded-xl overflow-hidden max-w-xs relative hover:scale-105 transition-transform duration-300').style('background: #6a0327; color: white;'):
        ui.image('./public/image/imagedisk.jpg').classes('w-full transition-transform duration-300 transform hover:scale-110')
        ui.label('DISK IMAGE Recovery').classes('text-xl font-semibold mt-2 mb-2 text-center')
        ui.label('Specialized software to recover files disk images.').classes('text-sm mb-4 px-4')
        ui.button('Buy Now', on_click=lambda: ui.notify('Redirecting to EWF Recovery purchase page')).classes('bg-yellow-500 text-white mx-4 mb-4')
    
    with ui.card().classes('shadow-xl rounded-xl overflow-hidden max-w-xs relative hover:scale-105 transition-transform duration-300').style('background: #6a0580; color: white;'):
        ui.image('./public/image/combined.jpg').classes('w-full transition-transform duration-300 transform hover:scale-110')
        ui.label('All in one Recovery').classes('text-xl font-semibold mt-2 mb-2 text-center')
        ui.label('Specialized combined software to recover data from various disk and file formats .').classes('text-sm mb-4 px-4')
        ui.button('Buy Now', on_click=lambda: ui.notify('Redirecting to EWF Recovery purchase page')).classes('bg-yellow-500 text-white mx-4 mb-4')


from nicegui import ui

# Footer Section with Updated Styling and Modern Icons
with ui.row().style('background: #2b2b2b; padding: 50px 24px; color: white; justify-content: center; align-items: center; flex-wrap: wrap; width: 100vw; margin: 0; text-align: center;'):

    # Main Logo or Brand Name
    ui.label('NIBBLE TOOLS Data Recovery').classes('text-3xl font-bold mb-2 text-gray-100')

    # Description or Tagline
    ui.label('Your trusted partner for data recovery solutions - HDD, SSD, RAID & more').classes('text-lg mb-6 text-gray-400')

    # Social Media Icons with Modern Styling
    with ui.row().style('gap: 30px; justify-content: center; margin-bottom: 30px; width: 100%;'):
        social_links = [
            ('https://facebook.com', 'fa-brands fa-facebook-f', '#1877f2'),
            ('https://twitter.com', 'fa-brands fa-twitter', '#1da1f2'),
            ('https://linkedin.com', 'fa-brands fa-linkedin-in', '#0077b5'),
            ('https://instagram.com', 'fa-brands fa-instagram', '#e4405f')
        ]
        for link, icon, color in social_links:
            with ui.link(link).classes('hover:scale-110 transition-transform duration-200'):
                ui.icon(icon).style(f'font-size: 30px; color: {color}; cursor: pointer;')

    # Quick Navigation Links
    with ui.row().style('gap: 30px; justify-content: center; flex-wrap: wrap; width: 100%; margin-bottom: 20px;'):
        ui.label('Privacy Policy').classes('text-sm cursor-pointer hover:text-gray-300').style('margin: 0 10px; font-weight: 500;')
        ui.label('Terms of Service').classes('text-sm cursor-pointer hover:text-gray-300').style('margin: 0 10px; font-weight: 500;')
        ui.label('Contact Us').classes('text-sm cursor-pointer hover:text-gray-300').style('margin: 0 10px; font-weight: 500;')
        ui.label('Support Center').classes('text-sm cursor-pointer hover:text-gray-300').style('margin: 0 10px; font-weight: 500;')

    # Footer Bottom Text
    ui.separator().style('margin: 20px 0; background: #444; height: 1px; width: 100%;')
    ui.label('© 2024 Professional Data Recovery. All Rights Reserved.').classes('text-sm text-gray-500 font-light')

if __name__ in {"__main__", "__mp_main__"}:
    ui.run()

