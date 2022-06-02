import os
import uuid

from django.utils.timezone import now


def uploaded_filepath(instance, filename):
    """
    Returns default filepath for uploaded files.
    """
    ext = filename.split(".")[-1]
    filename = "%s.%s" % (uuid.uuid4(), ext)
    today = now().strftime("%Y-%m-%d")
    return os.path.join("cms_files", today, filename)


def test_func_summernote_upload_view(request):
    return request.user.is_authenticated


SUMMERNOTE_THEME = "bs4"
SUMMERNOTE_CONFIG = {
    # Using SummernoteWidget - iframe mode, default
    "iframe": False,
    # # Or, you can set it as False to use SummernoteInplaceWidget by default - no iframe mode
    # # In this case, you have to load Bootstrap/jQuery stuff by manually.
    # # Use this when you're already using Bootstraip/jQuery based themes.
    # 'iframe': False,
    # You can put custom Summernote settings
    "summernote": {
        "prettifyHtml": True,
        # As an example, using Summernote Air-mode
        "airMode": False,
        # Change editor size
        "width": "100%",
        "height": "480",
        # Use proper language setting automatically (default)
        "lang": None,
        "toolbar": [
            ["style", ["style"]],
            [
                "font",
                [
                    "bold",
                    "italic",
                    "underline",
                    "superscript",
                    "subscript",
                    "strikethrough",
                    "clear",
                ],
            ],
            ["fontname", ["fontname"]],
            ["fontsize", ["fontsize"]],
            ["color", ["color"]],
            ["para", ["ul", "ol", "paragraph"]],
            ["height", ["height"]],
            ["table", ["table"]],
            ["insert", ["link", "picture", "video", "hr"]],
            ["view", ["fullscreen", "codeview"]],
        ],
        "fontNames": [
            "Arial",
            '"Arial Black"',
            "Comic Sans MS",
            "Courier New",
            "Helvetica Neue",
            "Helvetica",
            "Impact",
            "Lucida Grande",
            "Tahoma",
            "Times New Roman",
            "Verdana",
            "Trebuchet MS",
        ],
        "fontNamesIgnoreCheck": [
            "Arial",
            '"Arial Black"',
            "Comic Sans MS",
            "Courier New",
            "Helvetica Neue",
            "Helvetica",
            "Impact",
            "Lucida Grande",
            "Tahoma",
            "Times New Roman",
            "Verdana",
            "Trebuchet MS",
        ],
        "fontSizes": [
            "8",
            "9",
            "10",
            "11",
            "12",
            "14",
            "16",
            "18",
            "20",
            "22",
            "24",
            "27",
            "30",
            "32",
            "34",
            "36",
            "39",
            "43",
            "45",
            "48",
            "50",
        ],
        "codemirror": {
            "mode": "htmlmixed",
            "lineNumbers": True,
            "lineWrapping": True,
            "theme": "monokai",
        },
    },
    # dont delete empty codemirror!
    "codemirror": {},
    # Need authentication while uploading attachments.
    "attachment_require_authentication": True,
    # # Set `upload_to` function for attachments.
    "attachment_upload_to": uploaded_filepath,
    # test_func in summernote upload view. (Allow upload images only when user passes the test)
    # https://docs.djangoproject.com/en/2.2/topics/auth/default/#django.contrib.auth.mixins.UserPassesTestMixin
    "test_func_upload_view": test_func_summernote_upload_view,
    #
    # # Set custom storage class for attachments.
    # 'attachment_storage_class': 'my.custom.storage.class.name',
    #
    # # Set custom model for attachments (default: 'django_summernote.Attachment')
    # 'attachment_model': 'my.custom.attachment.model', # must inherit 'django_summernote.AbstractAttachment'
    # You can disable attachment feature.
    "disable_attachment": False,
    "js": (),
    # You can also add custom css/js for SummernoteInplaceWidget.
    # !!! Be sure to put {{ form.media }} in template before initiate summernote.
    "css_for_inplace": (),
    "js_for_inplace": (),
    # Codemirror as codeview
    # If any codemirror settings are defined, it will include codemirror files automatically.
    "css": (
        "//cdnjs.cloudflare.com/ajax/libs/codemirror/5.29.0/theme/monokai.min.css",
    ),
    "lazy": False,
}
