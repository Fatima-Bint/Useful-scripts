import os
from contextlib import contextmanager

from pylatex import Command, Document, MiniPage, Package, StandAloneGraphic
from pylatex.base_classes.command import Options
from pylatex.basic import FootnoteText, LineBreak, MediumText
from pylatex.position import Center, VerticalSpace
from pylatex.table import MultiRow, Tabular, Tabularx
from pylatex.utils import NoEscape, bold, escape_latex

BASE_DIR = os.path.dirname(__file__)

DISCLAIMER = """This report is only an opinion of GRADIA’s gemologist. The results are based on GRADIA’s professional technique and equipment. The stone in this report is a natural diamond and is not lab grown or a stimulant. Results from this report cannot be used as a guarantee, warranty, or valuation. For important limitations & disclaimers, please refer to www.gradia.net/terms."""


@contextmanager
def column_with_margin(doc):
    with doc.create(MiniPage(width=r"0.33333\textwidth", pos="t", content_pos="t", align="c")) as outer_page:
        with outer_page.create(MiniPage(width=r"0.9\textwidth", pos="t", content_pos="t", align="l")) as page:
            yield page


def hyperlink(url, text):
    text = escape_latex(text)
    return NoEscape(r"\color{MyBlue}\href{" + url + "}{" + text + "}")


@contextmanager
def change_color(doc, color):
    doc.append(Command("color", arguments=color))
    yield
    doc.append(Command("color", arguments="MyDarkGrey"))


def add_space_plus_new_line(doc, ems):
    doc.append(VerticalSpace(f"{ems}em"))
    doc.append(LineBreak())


def make_heading_divider(doc, heading_phrase):
    with change_color(doc, "MyBlue"):
        doc.append(bold(heading_phrase.lstrip().upper() + "\n"))
        doc.append(NoEscape(r"\noindent\rule{\textwidth}{0.5mm}"))
        add_space_plus_new_line(doc, 1)


def setup_colors(doc):
    doc.packages.append(Package("xcolor", options="table"))
    doc.append(Command("definecolor", arguments=["MyLightGrey", "RGB", "235, 235, 235"]))
    doc.append(Command("definecolor", arguments=["MyMidGrey", "RGB", "110, 110, 110"]))
    doc.append(Command("definecolor", arguments=["MyDarkGrey", "RGB", "52, 64, 68"]))
    doc.append(Command("definecolor", arguments=["MyBlue", "RGB", "65, 169, 156"]))


def add_left_column(doc):
    with column_with_margin(doc) as page:
        with page.create(Center()) as c:
            c.append(StandAloneGraphic(image_options="width=130px", filename=os.path.join(BASE_DIR, "logo.png")))
            add_space_plus_new_line(c, 1.5)
            c.append(MediumText(bold("Triple Verified Grading Report")))
            add_space_plus_new_line(c, 0.7)
            c.append(MediumText("No.: G00000013"))
            add_space_plus_new_line(c, 0.5)

        table = Tabular("l l", row_height=1.3)
        qr_code = StandAloneGraphic(image_options="width=50px", filename=os.path.join(BASE_DIR, "qr_code.png"))
        table.add_row(MultiRow(3, data=qr_code), "View digital report at:")
        table.add_row("", hyperlink("https://www.gradia.net/verify/G00000013", "gradia.net/verify"))
        table.add_row("", "and also on the blockchain")
        page.append(table)

        # we want to match this with the center line
        add_space_plus_new_line(page, 2.5)

        make_heading_divider(page, "report details")
        table = Tabular("l l", row_height=1.5, col_space="1em")
        table.add_row("Origin Testing", bold("Natural"))
        table.add_row("Shape & Cutting", bold("Round Brilliant"))
        table.add_row("Measurements", bold("2.89 - 2.92 x 1.802"))
        page.append(table)

        add_space_plus_new_line(page, 2)
        make_heading_divider(page, "diamond attributes")

        table = Tabular("l l l l", row_height=1.5, col_space="1em")
        table.add_row("Carat", "Color", "Clarity", "Fluoresence")
        table.add_row(bold("0.09"), bold("F"), bold("VS2"), bold("None"))
        page.append(table)
        add_space_plus_new_line(page, 1.5)
        table = Tabular("l l l", row_height=1.5, col_space="1em")
        table.add_row("Cut", "Polish", "Symmetry")
        table.add_row(bold("Very Good"), bold("Very Good"), bold("Good"))
        page.append(table)

        add_space_plus_new_line(page, 2)
        make_heading_divider(page, "comments")
        page.append(bold("This is a sample report."))
        page.append(LineBreak())
        page.append(bold("This is a second sentence."))


def add_center_column(doc):
    with column_with_margin(doc) as page:
        make_heading_divider(page, "ownership details")
        table = Tabular("l l", row_height=1.5, col_space="1em")
        table.add_row(MultiRow(2, data="Owner"), bold("GRADIA Laboratory"))
        table.add_row("", "(as of 8-Sep-20)")
        table.add_row("Goldway Ref", bold("SIOT202007002-R"))
        table.add_row("GIA Ref", bold("1231233345"))
        table.add_row("Blockchain Ref", bold("123154647sdiuyfh"))
        page.append(table)

        add_space_plus_new_line(page, 2)
        make_heading_divider(page, "macro image")
        macro_file = os.path.join(BASE_DIR, "macro.png")
        page.append(StandAloneGraphic(image_options="width=200px", filename=macro_file))

        add_space_plus_new_line(page, 2)
        make_heading_divider(page, "nano etching")

        table = Tabular("l l l", row_height=1.3, col_space="0.3em")
        nano_picture = StandAloneGraphic(image_options="width=70px", filename=os.path.join(BASE_DIR, "nano.png"))
        table.add_row("", "", MultiRow(3, data=nano_picture))
        table.add_row("Etched ID no.", bold("G00000013"), "")
        table.add_empty_row()
        page.append(table)


def add_right_column(doc):
    with column_with_margin(doc) as page:
        make_heading_divider(page, "diamond proportions")
        page.append(StandAloneGraphic(image_options="width=200px", filename=os.path.join(BASE_DIR, "diagram.png")))
        add_space_plus_new_line(page, 1)

        table = Tabular("l l", row_height=1.1, col_space="1em")
        table.add_row("Total Depth", bold("61.5%"))
        table.add_row("Table", bold("59%"))
        table.add_row("Star Length)", bold("45%"))
        table.add_row("Crown Angle", bold("34.5°"))
        table.add_row("Crown Height", bold("14%"))
        table.add_row("Pavilion Angle", bold("41.4°"))
        table.add_row("Pavilion Angle", bold("44%"))
        table.add_row("Lower Half", bold("75%"))
        table.add_row("Girdle Thickness", bold("3.5%"))
        table.add_row("Girdle Min", bold("Medium"))
        table.add_row("Girdle Max", bold("Slightly Thick"))
        table.add_row("Culet", bold("Very Small"))
        page.append(table)

        add_space_plus_new_line(page, 2)
        make_heading_divider(page, "inclusions")
        page.append(bold("Crystal, Feather"))

        add_space_plus_new_line(page, 1)
        page.append(NoEscape(r"\setstretch{0.7}"))
        page.append(FootnoteText(DISCLAIMER))


if __name__ == "__main__":
    doc = Document(
        documentclass=Command("documentclass", options=["12pt", "landscape"], arguments=["article"]),
        geometry_options={"margin": "0em", "includehead": False, "head": "0em", "includefoot": True, "foot": "3em"},
    )
    # doc.preamble.append(Command("usepackage", "helvet"))
    doc.append(NoEscape(r"\renewcommand{\footnotesize}{\fontsize{6pt}{6pt}\selectfont}"))

    setup_colors(doc)
    doc.packages.append(Package("hyperref", options=Options(colorlinks=False, allbordercolors="white")))
    doc.packages.append(Package("setspace"))
    with change_color(doc, "white"):
        doc.append(NoEscape(r"\noindent\rule{\textwidth}{0.5mm}"))
        add_space_plus_new_line(doc, 1)

    with doc.create(MiniPage(width=r"1\textwidth", pos="t", content_pos="t", align="l")) as page:
        add_left_column(page)
        add_center_column(page)
        add_right_column(page)

    doc.generate_pdf("sample_report", clean_tex=False)
