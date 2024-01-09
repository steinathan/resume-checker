""""
Slightly modified version from: https://github.com/louisgregg/ats-resume-generator
"""
from typing import Dict

from docxtpl import DocxTemplate, RichText
import re
import pprint

from app.prompts.resume_fixer import StructuredResume


def gen_filename(txt: str, extension: str) -> str:
    return re.sub('[^0-9a-zA-Z ]+', '', txt.lower()).replace(' ', '_') + '.' + extension


def render_intro_links(intro: Dict[str, str], template):
    if hasattr(intro, "linkedin"):
        rt = RichText()
        rt.add(
            text="LinkedIn",
            size="30px",
            underline=True,
            style="SubtleReference",
            font="Garamond",
            url_id=template.build_url_id(intro['linkedin']),
        )
        intro["linkedin"] = rt

    return intro


def render_project_links(project_list, template):
    """ render the `projectList` list into RichText with embedded links """
    project_list_combined = []
    if not project_list:
        return project_list_combined

    for project in project_list:
        rich_text_string = RichText(project['description'])
        if 'link' in project and 'code' in project:
            rich_text_string.add(' - ')
            rich_text_string.add(
                'link', url_id=template.build_url_id(project['link']))
            rich_text_string.add(', ')
            rich_text_string.add(
                'code', url_id=template.build_url_id(project['code']))
        elif 'link' in project:
            rich_text_string.add(' - ')
            rich_text_string.add(
                'link', url_id=template.build_url_id(project['link']))
            rich_text_string.add('.')
        elif 'code' in project:
            rich_text_string.add(' - ')
            rich_text_string.add(
                'code', url_id=template.build_url_id(project['code']))
            rich_text_string.add('.')
        else:
            rich_text_string.add('.')
        project_list_combined.append(rich_text_string)
    return project_list_combined


def build_resume(template_path: str, resume: StructuredResume) -> str:
    """ builds the resume and returns the path where its saved """
    context = resume.model_dump()
    template = DocxTemplate(template_path)

    if True:
        pp = pprint.PrettyPrinter(indent=2)
        pp.pprint(context)

    # render links as click-able hyperlinks using the richTextString class
    if hasattr(context, 'projectList'):
        context['projects'] = render_project_links(context['projectList'], template)

    docx_file = gen_filename(context['intro']['personName'], 'docx')
    print(f"Generating resume document: {docx_file}")

    template.render(context)
    template.save(docx_file)
    return docx_file
