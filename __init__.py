from qgis.gui import QgsGui, QgsCodeEditorColorScheme
from qgis.PyQt.QtGui import QColor


def classFactory(iface):
    return MonokaiProSpectrumSchemePlugin(iface)


class MonokaiProSpectrumScheme(QgsCodeEditorColorScheme):
    COLORS = {
        QgsCodeEditorColorScheme.ColorRole.Default: QColor('#f7f1ff'),
        QgsCodeEditorColorScheme.ColorRole.Keyword: QColor('#fc618d'),
        QgsCodeEditorColorScheme.ColorRole.Class: QColor('#5ad4e6'),
        QgsCodeEditorColorScheme.ColorRole.Method: QColor('#7bd88f'),
        QgsCodeEditorColorScheme.ColorRole.Decoration: QColor('#FD9353'),
        QgsCodeEditorColorScheme.ColorRole.Number: QColor('#948ae3'),
        QgsCodeEditorColorScheme.ColorRole.Comment: QColor('#69676c'),
        QgsCodeEditorColorScheme.ColorRole.CommentLine: QColor('#69676c'),
        QgsCodeEditorColorScheme.ColorRole.CommentBlock: QColor('#69676c'),
        QgsCodeEditorColorScheme.ColorRole.Background: QColor('#212121'),
        QgsCodeEditorColorScheme.ColorRole.Cursor: QColor('#f7f1ff'),
        QgsCodeEditorColorScheme.ColorRole.CaretLine: QColor('#363636'),
        QgsCodeEditorColorScheme.ColorRole.Operator: QColor('#939293'),
        QgsCodeEditorColorScheme.ColorRole.QuotedOperator: QColor('#939293'),
        QgsCodeEditorColorScheme.ColorRole.Identifier: QColor('#f7f1ff'),
        QgsCodeEditorColorScheme.ColorRole.QuotedIdentifier: QColor('#f7f1ff'),
        QgsCodeEditorColorScheme.ColorRole.Tag: QColor('#939293'),
        QgsCodeEditorColorScheme.ColorRole.UnknownTag: QColor('#fe4450'),
        QgsCodeEditorColorScheme.ColorRole.SingleQuote: QColor('#ffd866'),
        QgsCodeEditorColorScheme.ColorRole.DoubleQuote: QColor('#ffd866'),
        QgsCodeEditorColorScheme.ColorRole.TripleSingleQuote: QColor('#ffd866'),
        QgsCodeEditorColorScheme.ColorRole.TripleDoubleQuote: QColor('#69676c'),
        QgsCodeEditorColorScheme.ColorRole.MarginBackground: QColor('#212121'),
        QgsCodeEditorColorScheme.ColorRole.MarginForeground: QColor('#939293'),
        QgsCodeEditorColorScheme.ColorRole.SelectionBackground: QColor('#43474a'),
        QgsCodeEditorColorScheme.ColorRole.SelectionForeground: QColor('#f7f1ff'),
        QgsCodeEditorColorScheme.ColorRole.MatchedBraceBackground: QColor('#43474a'),
        QgsCodeEditorColorScheme.ColorRole.MatchedBraceForeground: QColor('#939293'),
        QgsCodeEditorColorScheme.ColorRole.Edge: QColor('#69676c'),
        QgsCodeEditorColorScheme.ColorRole.Fold: QColor('#212121'),
        QgsCodeEditorColorScheme.ColorRole.Error: QColor('#fe4450'),
        QgsCodeEditorColorScheme.ColorRole.FoldIconForeground: QColor('#69676c'),
        QgsCodeEditorColorScheme.ColorRole.FoldIconHalo: QColor('#212121'),
        QgsCodeEditorColorScheme.ColorRole.IndentationGuide: QColor('#939293'),
        QgsCodeEditorColorScheme.ColorRole.ErrorBackground: QColor('#f7f1ff'),
    }

    def __init__(self):
        super().__init__('Monokai Pro (Spectrum)', 'Monokai Pro (Spectrum)')

        for role, color in self.COLORS.items():
            self.setColor(role, color)


class MonokaiProSpectrumSchemePlugin:
    def __init__(self, _):
        QgsGui.codeEditorColorSchemeRegistry().addColorScheme(MonokaiProSpectrumScheme())

    def initGui(self):
        pass

    def unload(self):
        QgsGui.codeEditorColorSchemeRegistry().removeColorScheme('Monokai Pro (Spectrum)')
