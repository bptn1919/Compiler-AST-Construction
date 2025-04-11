# Generated from main/minigo/parser/MiniGo.g4 by ANTLR 4.9.2
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
    from typing import TextIO
else:
    from typing.io import TextIO


#2212416
from lexererr import *



def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2A")
        buf.write("\u01fc\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30")
        buf.write("\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36")
        buf.write("\t\36\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%")
        buf.write("\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.")
        buf.write("\t.\4/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64")
        buf.write("\t\64\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\4:\t:")
        buf.write("\4;\t;\4<\t<\4=\t=\4>\t>\4?\t?\4@\t@\4A\tA\4B\tB\3\2\3")
        buf.write("\2\3\2\3\3\3\3\3\3\3\4\3\4\3\5\3\5\3\5\3\6\3\6\3\7\3\7")
        buf.write("\3\7\3\b\3\b\3\b\3\t\3\t\3\t\3\n\3\n\3\n\3\13\3\13\3\13")
        buf.write("\3\f\3\f\3\f\3\r\3\r\3\r\3\16\3\16\3\17\3\17\3\20\3\20")
        buf.write("\3\21\3\21\3\22\3\22\3\23\3\23\3\23\3\24\3\24\3\24\3\25")
        buf.write("\3\25\3\26\3\26\3\27\3\27\3\30\3\30\3\31\3\31\3\32\3\32")
        buf.write("\3\33\3\33\3\34\3\34\3\35\3\35\3\36\3\36\3\37\3\37\3 ")
        buf.write("\3 \3!\3!\3\"\3\"\3\"\3#\3#\3#\3#\3#\3$\3$\3$\3$\3%\3")
        buf.write("%\3%\3%\3%\3%\3%\3&\3&\3&\3&\3&\3\'\3\'\3\'\3\'\3\'\3")
        buf.write("(\3(\3(\3(\3(\3(\3(\3)\3)\3)\3)\3)\3)\3)\3)\3)\3)\3*\3")
        buf.write("*\3*\3*\3*\3*\3*\3+\3+\3+\3+\3,\3,\3,\3,\3,\3,\3-\3-\3")
        buf.write("-\3-\3-\3-\3-\3-\3.\3.\3.\3.\3.\3.\3/\3/\3/\3/\3\60\3")
        buf.write("\60\3\60\3\60\3\60\3\60\3\60\3\60\3\60\3\61\3\61\3\61")
        buf.write("\3\61\3\61\3\61\3\62\3\62\3\62\3\62\3\62\3\62\3\63\3\63")
        buf.write("\3\63\3\63\3\64\3\64\3\64\3\64\3\64\3\65\3\65\3\65\3\65")
        buf.write("\3\65\3\65\3\66\5\66\u0148\n\66\3\66\3\66\3\67\3\67\7")
        buf.write("\67\u014e\n\67\f\67\16\67\u0151\13\67\38\38\38\78\u0156")
        buf.write("\n8\f8\168\u0159\138\38\38\38\38\68\u015f\n8\r8\168\u0160")
        buf.write("\38\38\38\38\68\u0167\n8\r8\168\u0168\38\38\38\38\68\u016f")
        buf.write("\n8\r8\168\u0170\38\38\38\38\68\u0177\n8\r8\168\u0178")
        buf.write("\38\38\38\38\68\u017f\n8\r8\168\u0180\38\38\38\38\68\u0187")
        buf.write("\n8\r8\168\u0188\58\u018b\n8\39\69\u018e\n9\r9\169\u018f")
        buf.write("\39\39\79\u0194\n9\f9\169\u0197\139\39\39\59\u019b\n9")
        buf.write("\39\69\u019e\n9\r9\169\u019f\59\u01a2\n9\3:\3:\3:\7:\u01a7")
        buf.write("\n:\f:\16:\u01aa\13:\3:\3:\3;\3;\3;\3;\3;\3;\3;\3;\3;")
        buf.write("\3;\5;\u01b8\n;\3<\3<\3<\3<\7<\u01be\n<\f<\16<\u01c1\13")
        buf.write("<\3<\3<\3<\5<\u01c6\n<\3<\3<\3=\3=\3=\3=\7=\u01ce\n=\f")
        buf.write("=\16=\u01d1\13=\3=\3=\3=\3=\3>\6>\u01d8\n>\r>\16>\u01d9")
        buf.write("\3>\3>\3?\3?\3?\3?\7?\u01e2\n?\f?\16?\u01e5\13?\3?\3?")
        buf.write("\3@\3@\3@\3@\3@\7@\u01ee\n@\f@\16@\u01f1\13@\3@\3@\3@")
        buf.write("\3A\3A\3A\3A\3B\3B\3B\3\u01ef\2C\3\3\5\4\7\5\t\6\13\7")
        buf.write("\r\b\17\t\21\n\23\13\25\f\27\r\31\16\33\17\35\20\37\21")
        buf.write("!\22#\23%\24\'\25)\26+\27-\30/\31\61\32\63\33\65\34\67")
        buf.write("\359\36;\37= ?!A\"C#E$G%I&K\'M(O)Q*S+U,W-Y.[/]\60_\61")
        buf.write("a\62c\63e\64g\65i\66k\67m8o9q:s;u\2w<y={>}?\177\2\u0081")
        buf.write("@\u0083A\3\2\21\5\2C\\aac|\6\2\62;C\\aac|\3\2\63;\3\2")
        buf.write("\62;\3\2\62\63\3\2\629\5\2\62;CHch\4\2GGgg\4\2--//\6\2")
        buf.write("\f\f\17\17$$^^\5\2\f\f$$^^\7\2$$^^ppttvv\3\3\f\f\5\2\13")
        buf.write("\13\16\16\"\"\4\2\f\f\17\17\2\u021d\2\3\3\2\2\2\2\5\3")
        buf.write("\2\2\2\2\7\3\2\2\2\2\t\3\2\2\2\2\13\3\2\2\2\2\r\3\2\2")
        buf.write("\2\2\17\3\2\2\2\2\21\3\2\2\2\2\23\3\2\2\2\2\25\3\2\2\2")
        buf.write("\2\27\3\2\2\2\2\31\3\2\2\2\2\33\3\2\2\2\2\35\3\2\2\2\2")
        buf.write("\37\3\2\2\2\2!\3\2\2\2\2#\3\2\2\2\2%\3\2\2\2\2\'\3\2\2")
        buf.write("\2\2)\3\2\2\2\2+\3\2\2\2\2-\3\2\2\2\2/\3\2\2\2\2\61\3")
        buf.write("\2\2\2\2\63\3\2\2\2\2\65\3\2\2\2\2\67\3\2\2\2\29\3\2\2")
        buf.write("\2\2;\3\2\2\2\2=\3\2\2\2\2?\3\2\2\2\2A\3\2\2\2\2C\3\2")
        buf.write("\2\2\2E\3\2\2\2\2G\3\2\2\2\2I\3\2\2\2\2K\3\2\2\2\2M\3")
        buf.write("\2\2\2\2O\3\2\2\2\2Q\3\2\2\2\2S\3\2\2\2\2U\3\2\2\2\2W")
        buf.write("\3\2\2\2\2Y\3\2\2\2\2[\3\2\2\2\2]\3\2\2\2\2_\3\2\2\2\2")
        buf.write("a\3\2\2\2\2c\3\2\2\2\2e\3\2\2\2\2g\3\2\2\2\2i\3\2\2\2")
        buf.write("\2k\3\2\2\2\2m\3\2\2\2\2o\3\2\2\2\2q\3\2\2\2\2s\3\2\2")
        buf.write("\2\2w\3\2\2\2\2y\3\2\2\2\2{\3\2\2\2\2}\3\2\2\2\2\u0081")
        buf.write("\3\2\2\2\2\u0083\3\2\2\2\3\u0085\3\2\2\2\5\u0088\3\2\2")
        buf.write("\2\7\u008b\3\2\2\2\t\u008d\3\2\2\2\13\u0090\3\2\2\2\r")
        buf.write("\u0092\3\2\2\2\17\u0095\3\2\2\2\21\u0098\3\2\2\2\23\u009b")
        buf.write("\3\2\2\2\25\u009e\3\2\2\2\27\u00a1\3\2\2\2\31\u00a4\3")
        buf.write("\2\2\2\33\u00a7\3\2\2\2\35\u00a9\3\2\2\2\37\u00ab\3\2")
        buf.write("\2\2!\u00ad\3\2\2\2#\u00af\3\2\2\2%\u00b1\3\2\2\2\'\u00b4")
        buf.write("\3\2\2\2)\u00b7\3\2\2\2+\u00b9\3\2\2\2-\u00bb\3\2\2\2")
        buf.write("/\u00bd\3\2\2\2\61\u00bf\3\2\2\2\63\u00c1\3\2\2\2\65\u00c3")
        buf.write("\3\2\2\2\67\u00c5\3\2\2\29\u00c7\3\2\2\2;\u00c9\3\2\2")
        buf.write("\2=\u00cb\3\2\2\2?\u00cd\3\2\2\2A\u00cf\3\2\2\2C\u00d1")
        buf.write("\3\2\2\2E\u00d4\3\2\2\2G\u00d9\3\2\2\2I\u00dd\3\2\2\2")
        buf.write("K\u00e4\3\2\2\2M\u00e9\3\2\2\2O\u00ee\3\2\2\2Q\u00f5\3")
        buf.write("\2\2\2S\u00ff\3\2\2\2U\u0106\3\2\2\2W\u010a\3\2\2\2Y\u0110")
        buf.write("\3\2\2\2[\u0118\3\2\2\2]\u011e\3\2\2\2_\u0122\3\2\2\2")
        buf.write("a\u012b\3\2\2\2c\u0131\3\2\2\2e\u0137\3\2\2\2g\u013b\3")
        buf.write("\2\2\2i\u0140\3\2\2\2k\u0147\3\2\2\2m\u014b\3\2\2\2o\u018a")
        buf.write("\3\2\2\2q\u018d\3\2\2\2s\u01a3\3\2\2\2u\u01b7\3\2\2\2")
        buf.write("w\u01b9\3\2\2\2y\u01c9\3\2\2\2{\u01d7\3\2\2\2}\u01dd\3")
        buf.write("\2\2\2\177\u01e8\3\2\2\2\u0081\u01f5\3\2\2\2\u0083\u01f9")
        buf.write("\3\2\2\2\u0085\u0086\7?\2\2\u0086\u0087\7?\2\2\u0087\4")
        buf.write("\3\2\2\2\u0088\u0089\7#\2\2\u0089\u008a\7?\2\2\u008a\6")
        buf.write("\3\2\2\2\u008b\u008c\7>\2\2\u008c\b\3\2\2\2\u008d\u008e")
        buf.write("\7>\2\2\u008e\u008f\7?\2\2\u008f\n\3\2\2\2\u0090\u0091")
        buf.write("\7@\2\2\u0091\f\3\2\2\2\u0092\u0093\7@\2\2\u0093\u0094")
        buf.write("\7?\2\2\u0094\16\3\2\2\2\u0095\u0096\7<\2\2\u0096\u0097")
        buf.write("\7?\2\2\u0097\20\3\2\2\2\u0098\u0099\7-\2\2\u0099\u009a")
        buf.write("\7?\2\2\u009a\22\3\2\2\2\u009b\u009c\7/\2\2\u009c\u009d")
        buf.write("\7?\2\2\u009d\24\3\2\2\2\u009e\u009f\7,\2\2\u009f\u00a0")
        buf.write("\7?\2\2\u00a0\26\3\2\2\2\u00a1\u00a2\7\61\2\2\u00a2\u00a3")
        buf.write("\7?\2\2\u00a3\30\3\2\2\2\u00a4\u00a5\7\'\2\2\u00a5\u00a6")
        buf.write("\7?\2\2\u00a6\32\3\2\2\2\u00a7\u00a8\7-\2\2\u00a8\34\3")
        buf.write("\2\2\2\u00a9\u00aa\7/\2\2\u00aa\36\3\2\2\2\u00ab\u00ac")
        buf.write("\7,\2\2\u00ac \3\2\2\2\u00ad\u00ae\7\61\2\2\u00ae\"\3")
        buf.write("\2\2\2\u00af\u00b0\7\'\2\2\u00b0$\3\2\2\2\u00b1\u00b2")
        buf.write("\7(\2\2\u00b2\u00b3\7(\2\2\u00b3&\3\2\2\2\u00b4\u00b5")
        buf.write("\7~\2\2\u00b5\u00b6\7~\2\2\u00b6(\3\2\2\2\u00b7\u00b8")
        buf.write("\7#\2\2\u00b8*\3\2\2\2\u00b9\u00ba\7?\2\2\u00ba,\3\2\2")
        buf.write("\2\u00bb\u00bc\7\60\2\2\u00bc.\3\2\2\2\u00bd\u00be\7=")
        buf.write("\2\2\u00be\60\3\2\2\2\u00bf\u00c0\7*\2\2\u00c0\62\3\2")
        buf.write("\2\2\u00c1\u00c2\7+\2\2\u00c2\64\3\2\2\2\u00c3\u00c4\7")
        buf.write("]\2\2\u00c4\66\3\2\2\2\u00c5\u00c6\7_\2\2\u00c68\3\2\2")
        buf.write("\2\u00c7\u00c8\7}\2\2\u00c8:\3\2\2\2\u00c9\u00ca\7\177")
        buf.write("\2\2\u00ca<\3\2\2\2\u00cb\u00cc\7.\2\2\u00cc>\3\2\2\2")
        buf.write("\u00cd\u00ce\7a\2\2\u00ce@\3\2\2\2\u00cf\u00d0\7<\2\2")
        buf.write("\u00d0B\3\2\2\2\u00d1\u00d2\7k\2\2\u00d2\u00d3\7h\2\2")
        buf.write("\u00d3D\3\2\2\2\u00d4\u00d5\7g\2\2\u00d5\u00d6\7n\2\2")
        buf.write("\u00d6\u00d7\7u\2\2\u00d7\u00d8\7g\2\2\u00d8F\3\2\2\2")
        buf.write("\u00d9\u00da\7h\2\2\u00da\u00db\7q\2\2\u00db\u00dc\7t")
        buf.write("\2\2\u00dcH\3\2\2\2\u00dd\u00de\7t\2\2\u00de\u00df\7g")
        buf.write("\2\2\u00df\u00e0\7v\2\2\u00e0\u00e1\7w\2\2\u00e1\u00e2")
        buf.write("\7t\2\2\u00e2\u00e3\7p\2\2\u00e3J\3\2\2\2\u00e4\u00e5")
        buf.write("\7h\2\2\u00e5\u00e6\7w\2\2\u00e6\u00e7\7p\2\2\u00e7\u00e8")
        buf.write("\7e\2\2\u00e8L\3\2\2\2\u00e9\u00ea\7v\2\2\u00ea\u00eb")
        buf.write("\7{\2\2\u00eb\u00ec\7r\2\2\u00ec\u00ed\7g\2\2\u00edN\3")
        buf.write("\2\2\2\u00ee\u00ef\7u\2\2\u00ef\u00f0\7v\2\2\u00f0\u00f1")
        buf.write("\7t\2\2\u00f1\u00f2\7w\2\2\u00f2\u00f3\7e\2\2\u00f3\u00f4")
        buf.write("\7v\2\2\u00f4P\3\2\2\2\u00f5\u00f6\7k\2\2\u00f6\u00f7")
        buf.write("\7p\2\2\u00f7\u00f8\7v\2\2\u00f8\u00f9\7g\2\2\u00f9\u00fa")
        buf.write("\7t\2\2\u00fa\u00fb\7h\2\2\u00fb\u00fc\7c\2\2\u00fc\u00fd")
        buf.write("\7e\2\2\u00fd\u00fe\7g\2\2\u00feR\3\2\2\2\u00ff\u0100")
        buf.write("\7u\2\2\u0100\u0101\7v\2\2\u0101\u0102\7t\2\2\u0102\u0103")
        buf.write("\7k\2\2\u0103\u0104\7p\2\2\u0104\u0105\7i\2\2\u0105T\3")
        buf.write("\2\2\2\u0106\u0107\7k\2\2\u0107\u0108\7p\2\2\u0108\u0109")
        buf.write("\7v\2\2\u0109V\3\2\2\2\u010a\u010b\7h\2\2\u010b\u010c")
        buf.write("\7n\2\2\u010c\u010d\7q\2\2\u010d\u010e\7c\2\2\u010e\u010f")
        buf.write("\7v\2\2\u010fX\3\2\2\2\u0110\u0111\7d\2\2\u0111\u0112")
        buf.write("\7q\2\2\u0112\u0113\7q\2\2\u0113\u0114\7n\2\2\u0114\u0115")
        buf.write("\7g\2\2\u0115\u0116\7c\2\2\u0116\u0117\7p\2\2\u0117Z\3")
        buf.write("\2\2\2\u0118\u0119\7e\2\2\u0119\u011a\7q\2\2\u011a\u011b")
        buf.write("\7p\2\2\u011b\u011c\7u\2\2\u011c\u011d\7v\2\2\u011d\\")
        buf.write("\3\2\2\2\u011e\u011f\7x\2\2\u011f\u0120\7c\2\2\u0120\u0121")
        buf.write("\7t\2\2\u0121^\3\2\2\2\u0122\u0123\7e\2\2\u0123\u0124")
        buf.write("\7q\2\2\u0124\u0125\7p\2\2\u0125\u0126\7v\2\2\u0126\u0127")
        buf.write("\7k\2\2\u0127\u0128\7p\2\2\u0128\u0129\7w\2\2\u0129\u012a")
        buf.write("\7g\2\2\u012a`\3\2\2\2\u012b\u012c\7d\2\2\u012c\u012d")
        buf.write("\7t\2\2\u012d\u012e\7g\2\2\u012e\u012f\7c\2\2\u012f\u0130")
        buf.write("\7m\2\2\u0130b\3\2\2\2\u0131\u0132\7t\2\2\u0132\u0133")
        buf.write("\7c\2\2\u0133\u0134\7p\2\2\u0134\u0135\7i\2\2\u0135\u0136")
        buf.write("\7g\2\2\u0136d\3\2\2\2\u0137\u0138\7p\2\2\u0138\u0139")
        buf.write("\7k\2\2\u0139\u013a\7n\2\2\u013af\3\2\2\2\u013b\u013c")
        buf.write("\7v\2\2\u013c\u013d\7t\2\2\u013d\u013e\7w\2\2\u013e\u013f")
        buf.write("\7g\2\2\u013fh\3\2\2\2\u0140\u0141\7h\2\2\u0141\u0142")
        buf.write("\7c\2\2\u0142\u0143\7n\2\2\u0143\u0144\7u\2\2\u0144\u0145")
        buf.write("\7g\2\2\u0145j\3\2\2\2\u0146\u0148\7\17\2\2\u0147\u0146")
        buf.write("\3\2\2\2\u0147\u0148\3\2\2\2\u0148\u0149\3\2\2\2\u0149")
        buf.write("\u014a\7\f\2\2\u014al\3\2\2\2\u014b\u014f\t\2\2\2\u014c")
        buf.write("\u014e\t\3\2\2\u014d\u014c\3\2\2\2\u014e\u0151\3\2\2\2")
        buf.write("\u014f\u014d\3\2\2\2\u014f\u0150\3\2\2\2\u0150n\3\2\2")
        buf.write("\2\u0151\u014f\3\2\2\2\u0152\u018b\7\62\2\2\u0153\u0157")
        buf.write("\t\4\2\2\u0154\u0156\t\5\2\2\u0155\u0154\3\2\2\2\u0156")
        buf.write("\u0159\3\2\2\2\u0157\u0155\3\2\2\2\u0157\u0158\3\2\2\2")
        buf.write("\u0158\u018b\3\2\2\2\u0159\u0157\3\2\2\2\u015a\u015b\7")
        buf.write("\62\2\2\u015b\u015c\7d\2\2\u015c\u015e\3\2\2\2\u015d\u015f")
        buf.write("\t\6\2\2\u015e\u015d\3\2\2\2\u015f\u0160\3\2\2\2\u0160")
        buf.write("\u015e\3\2\2\2\u0160\u0161\3\2\2\2\u0161\u018b\3\2\2\2")
        buf.write("\u0162\u0163\7\62\2\2\u0163\u0164\7D\2\2\u0164\u0166\3")
        buf.write("\2\2\2\u0165\u0167\t\6\2\2\u0166\u0165\3\2\2\2\u0167\u0168")
        buf.write("\3\2\2\2\u0168\u0166\3\2\2\2\u0168\u0169\3\2\2\2\u0169")
        buf.write("\u018b\3\2\2\2\u016a\u016b\7\62\2\2\u016b\u016c\7q\2\2")
        buf.write("\u016c\u016e\3\2\2\2\u016d\u016f\t\7\2\2\u016e\u016d\3")
        buf.write("\2\2\2\u016f\u0170\3\2\2\2\u0170\u016e\3\2\2\2\u0170\u0171")
        buf.write("\3\2\2\2\u0171\u018b\3\2\2\2\u0172\u0173\7\62\2\2\u0173")
        buf.write("\u0174\7Q\2\2\u0174\u0176\3\2\2\2\u0175\u0177\t\7\2\2")
        buf.write("\u0176\u0175\3\2\2\2\u0177\u0178\3\2\2\2\u0178\u0176\3")
        buf.write("\2\2\2\u0178\u0179\3\2\2\2\u0179\u018b\3\2\2\2\u017a\u017b")
        buf.write("\7\62\2\2\u017b\u017c\7z\2\2\u017c\u017e\3\2\2\2\u017d")
        buf.write("\u017f\t\b\2\2\u017e\u017d\3\2\2\2\u017f\u0180\3\2\2\2")
        buf.write("\u0180\u017e\3\2\2\2\u0180\u0181\3\2\2\2\u0181\u018b\3")
        buf.write("\2\2\2\u0182\u0183\7\62\2\2\u0183\u0184\7Z\2\2\u0184\u0186")
        buf.write("\3\2\2\2\u0185\u0187\t\b\2\2\u0186\u0185\3\2\2\2\u0187")
        buf.write("\u0188\3\2\2\2\u0188\u0186\3\2\2\2\u0188\u0189\3\2\2\2")
        buf.write("\u0189\u018b\3\2\2\2\u018a\u0152\3\2\2\2\u018a\u0153\3")
        buf.write("\2\2\2\u018a\u015a\3\2\2\2\u018a\u0162\3\2\2\2\u018a\u016a")
        buf.write("\3\2\2\2\u018a\u0172\3\2\2\2\u018a\u017a\3\2\2\2\u018a")
        buf.write("\u0182\3\2\2\2\u018bp\3\2\2\2\u018c\u018e\t\5\2\2\u018d")
        buf.write("\u018c\3\2\2\2\u018e\u018f\3\2\2\2\u018f\u018d\3\2\2\2")
        buf.write("\u018f\u0190\3\2\2\2\u0190\u0191\3\2\2\2\u0191\u0195\5")
        buf.write("-\27\2\u0192\u0194\t\5\2\2\u0193\u0192\3\2\2\2\u0194\u0197")
        buf.write("\3\2\2\2\u0195\u0193\3\2\2\2\u0195\u0196\3\2\2\2\u0196")
        buf.write("\u01a1\3\2\2\2\u0197\u0195\3\2\2\2\u0198\u019a\t\t\2\2")
        buf.write("\u0199\u019b\t\n\2\2\u019a\u0199\3\2\2\2\u019a\u019b\3")
        buf.write("\2\2\2\u019b\u019d\3\2\2\2\u019c\u019e\t\5\2\2\u019d\u019c")
        buf.write("\3\2\2\2\u019e\u019f\3\2\2\2\u019f\u019d\3\2\2\2\u019f")
        buf.write("\u01a0\3\2\2\2\u01a0\u01a2\3\2\2\2\u01a1\u0198\3\2\2\2")
        buf.write("\u01a1\u01a2\3\2\2\2\u01a2r\3\2\2\2\u01a3\u01a8\7$\2\2")
        buf.write("\u01a4\u01a7\5u;\2\u01a5\u01a7\n\13\2\2\u01a6\u01a4\3")
        buf.write("\2\2\2\u01a6\u01a5\3\2\2\2\u01a7\u01aa\3\2\2\2\u01a8\u01a6")
        buf.write("\3\2\2\2\u01a8\u01a9\3\2\2\2\u01a9\u01ab\3\2\2\2\u01aa")
        buf.write("\u01a8\3\2\2\2\u01ab\u01ac\7$\2\2\u01act\3\2\2\2\u01ad")
        buf.write("\u01ae\7^\2\2\u01ae\u01b8\7p\2\2\u01af\u01b0\7^\2\2\u01b0")
        buf.write("\u01b8\7v\2\2\u01b1\u01b2\7^\2\2\u01b2\u01b8\7t\2\2\u01b3")
        buf.write("\u01b4\7^\2\2\u01b4\u01b8\7$\2\2\u01b5\u01b6\7^\2\2\u01b6")
        buf.write("\u01b8\7^\2\2\u01b7\u01ad\3\2\2\2\u01b7\u01af\3\2\2\2")
        buf.write("\u01b7\u01b1\3\2\2\2\u01b7\u01b3\3\2\2\2\u01b7\u01b5\3")
        buf.write("\2\2\2\u01b8v\3\2\2\2\u01b9\u01bf\7$\2\2\u01ba\u01be\n")
        buf.write("\f\2\2\u01bb\u01bc\7^\2\2\u01bc\u01be\t\r\2\2\u01bd\u01ba")
        buf.write("\3\2\2\2\u01bd\u01bb\3\2\2\2\u01be\u01c1\3\2\2\2\u01bf")
        buf.write("\u01bd\3\2\2\2\u01bf\u01c0\3\2\2\2\u01c0\u01c5\3\2\2\2")
        buf.write("\u01c1\u01bf\3\2\2\2\u01c2\u01c6\t\16\2\2\u01c3\u01c4")
        buf.write("\7\17\2\2\u01c4\u01c6\7\f\2\2\u01c5\u01c2\3\2\2\2\u01c5")
        buf.write("\u01c3\3\2\2\2\u01c6\u01c7\3\2\2\2\u01c7\u01c8\b<\2\2")
        buf.write("\u01c8x\3\2\2\2\u01c9\u01cf\7$\2\2\u01ca\u01ce\n\f\2\2")
        buf.write("\u01cb\u01cc\7^\2\2\u01cc\u01ce\t\r\2\2\u01cd\u01ca\3")
        buf.write("\2\2\2\u01cd\u01cb\3\2\2\2\u01ce\u01d1\3\2\2\2\u01cf\u01cd")
        buf.write("\3\2\2\2\u01cf\u01d0\3\2\2\2\u01d0\u01d2\3\2\2\2\u01d1")
        buf.write("\u01cf\3\2\2\2\u01d2\u01d3\7^\2\2\u01d3\u01d4\n\r\2\2")
        buf.write("\u01d4\u01d5\b=\3\2\u01d5z\3\2\2\2\u01d6\u01d8\t\17\2")
        buf.write("\2\u01d7\u01d6\3\2\2\2\u01d8\u01d9\3\2\2\2\u01d9\u01d7")
        buf.write("\3\2\2\2\u01d9\u01da\3\2\2\2\u01da\u01db\3\2\2\2\u01db")
        buf.write("\u01dc\b>\4\2\u01dc|\3\2\2\2\u01dd\u01de\7\61\2\2\u01de")
        buf.write("\u01df\7\61\2\2\u01df\u01e3\3\2\2\2\u01e0\u01e2\n\20\2")
        buf.write("\2\u01e1\u01e0\3\2\2\2\u01e2\u01e5\3\2\2\2\u01e3\u01e1")
        buf.write("\3\2\2\2\u01e3\u01e4\3\2\2\2\u01e4\u01e6\3\2\2\2\u01e5")
        buf.write("\u01e3\3\2\2\2\u01e6\u01e7\b?\4\2\u01e7~\3\2\2\2\u01e8")
        buf.write("\u01e9\7\61\2\2\u01e9\u01ea\7,\2\2\u01ea\u01ef\3\2\2\2")
        buf.write("\u01eb\u01ee\5\177@\2\u01ec\u01ee\13\2\2\2\u01ed\u01eb")
        buf.write("\3\2\2\2\u01ed\u01ec\3\2\2\2\u01ee\u01f1\3\2\2\2\u01ef")
        buf.write("\u01f0\3\2\2\2\u01ef\u01ed\3\2\2\2\u01f0\u01f2\3\2\2\2")
        buf.write("\u01f1\u01ef\3\2\2\2\u01f2\u01f3\7,\2\2\u01f3\u01f4\7")
        buf.write("\61\2\2\u01f4\u0080\3\2\2\2\u01f5\u01f6\5\177@\2\u01f6")
        buf.write("\u01f7\3\2\2\2\u01f7\u01f8\bA\4\2\u01f8\u0082\3\2\2\2")
        buf.write("\u01f9\u01fa\13\2\2\2\u01fa\u01fb\bB\5\2\u01fb\u0084\3")
        buf.write("\2\2\2\36\2\u0147\u014f\u0157\u0160\u0168\u0170\u0178")
        buf.write("\u0180\u0188\u018a\u018f\u0195\u019a\u019f\u01a1\u01a6")
        buf.write("\u01a8\u01b7\u01bd\u01bf\u01c5\u01cd\u01cf\u01d9\u01e3")
        buf.write("\u01ed\u01ef\6\3<\2\3=\3\b\2\2\3B\4")
        return buf.getvalue()


class MiniGoLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    EQ = 1
    NEQ = 2
    LT = 3
    LE = 4
    GT = 5
    GE = 6
    ASSIGN_INIT = 7
    ADD_ASSIGN = 8
    SUB_ASSIGN = 9
    MUL_ASSIGN = 10
    DIV_ASSIGN = 11
    MOD_ASSIGN = 12
    PLUS = 13
    MINUS = 14
    MULT = 15
    DIV = 16
    MOD = 17
    AND = 18
    OR = 19
    NOT = 20
    ASSIGN = 21
    DOT = 22
    SEMI = 23
    LPAREN = 24
    RPAREN = 25
    LBRACK = 26
    RBRACK = 27
    LBRACE = 28
    RBRACE = 29
    COMMA = 30
    UNDERSCORE = 31
    COLON = 32
    KW_IF = 33
    KW_ELSE = 34
    KW_FOR = 35
    KW_RETURN = 36
    KW_FUNC = 37
    KW_TYPE = 38
    KW_STRUCT = 39
    KW_INTERFACE = 40
    KW_STRING = 41
    KW_INT = 42
    KW_FLOAT = 43
    KW_BOOLEAN = 44
    KW_CONST = 45
    KW_VAR = 46
    KW_CONTINUE = 47
    KW_BREAK = 48
    KW_RANGE = 49
    KW_NIL = 50
    KW_TRUE = 51
    KW_FALSE = 52
    NEWLINE = 53
    ID = 54
    INT_LIT = 55
    FLOAT_LIT = 56
    STRING_LIT = 57
    UNCLOSE_STRING = 58
    ILLEGAL_ESCAPE = 59
    WS = 60
    COMMENT = 61
    MULTILINE_COMMENT = 62
    ERROR_CHAR = 63

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'=='", "'!='", "'<'", "'<='", "'>'", "'>='", "':='", "'+='", 
            "'-='", "'*='", "'/='", "'%='", "'+'", "'-'", "'*'", "'/'", 
            "'%'", "'&&'", "'||'", "'!'", "'='", "'.'", "';'", "'('", "')'", 
            "'['", "']'", "'{'", "'}'", "','", "'_'", "':'", "'if'", "'else'", 
            "'for'", "'return'", "'func'", "'type'", "'struct'", "'interface'", 
            "'string'", "'int'", "'float'", "'boolean'", "'const'", "'var'", 
            "'continue'", "'break'", "'range'", "'nil'", "'true'", "'false'" ]

    symbolicNames = [ "<INVALID>",
            "EQ", "NEQ", "LT", "LE", "GT", "GE", "ASSIGN_INIT", "ADD_ASSIGN", 
            "SUB_ASSIGN", "MUL_ASSIGN", "DIV_ASSIGN", "MOD_ASSIGN", "PLUS", 
            "MINUS", "MULT", "DIV", "MOD", "AND", "OR", "NOT", "ASSIGN", 
            "DOT", "SEMI", "LPAREN", "RPAREN", "LBRACK", "RBRACK", "LBRACE", 
            "RBRACE", "COMMA", "UNDERSCORE", "COLON", "KW_IF", "KW_ELSE", 
            "KW_FOR", "KW_RETURN", "KW_FUNC", "KW_TYPE", "KW_STRUCT", "KW_INTERFACE", 
            "KW_STRING", "KW_INT", "KW_FLOAT", "KW_BOOLEAN", "KW_CONST", 
            "KW_VAR", "KW_CONTINUE", "KW_BREAK", "KW_RANGE", "KW_NIL", "KW_TRUE", 
            "KW_FALSE", "NEWLINE", "ID", "INT_LIT", "FLOAT_LIT", "STRING_LIT", 
            "UNCLOSE_STRING", "ILLEGAL_ESCAPE", "WS", "COMMENT", "MULTILINE_COMMENT", 
            "ERROR_CHAR" ]

    ruleNames = [ "EQ", "NEQ", "LT", "LE", "GT", "GE", "ASSIGN_INIT", "ADD_ASSIGN", 
                  "SUB_ASSIGN", "MUL_ASSIGN", "DIV_ASSIGN", "MOD_ASSIGN", 
                  "PLUS", "MINUS", "MULT", "DIV", "MOD", "AND", "OR", "NOT", 
                  "ASSIGN", "DOT", "SEMI", "LPAREN", "RPAREN", "LBRACK", 
                  "RBRACK", "LBRACE", "RBRACE", "COMMA", "UNDERSCORE", "COLON", 
                  "KW_IF", "KW_ELSE", "KW_FOR", "KW_RETURN", "KW_FUNC", 
                  "KW_TYPE", "KW_STRUCT", "KW_INTERFACE", "KW_STRING", "KW_INT", 
                  "KW_FLOAT", "KW_BOOLEAN", "KW_CONST", "KW_VAR", "KW_CONTINUE", 
                  "KW_BREAK", "KW_RANGE", "KW_NIL", "KW_TRUE", "KW_FALSE", 
                  "NEWLINE", "ID", "INT_LIT", "FLOAT_LIT", "STRING_LIT", 
                  "ESCAPE_SEQUENCE", "UNCLOSE_STRING", "ILLEGAL_ESCAPE", 
                  "WS", "COMMENT", "NESTED_COMMENT", "MULTILINE_COMMENT", 
                  "ERROR_CHAR" ]

    grammarFileName = "MiniGo.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.2")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


    prev_token = None

    def emit(self):
        tk = self.type

        if tk == self.UNCLOSE_STRING:       
            result = super().emit()
            raise UncloseString(result.text)
        elif tk == self.ILLEGAL_ESCAPE:
            result = super().emit()
            raise IllegalEscape(result.text)
        elif tk == self.ERROR_CHAR:
            result = super().emit()
            raise ErrorToken(result.text)
        elif tk == self.NEWLINE:
            # Kiểm tra nếu token trước tồn tại và thuộc một trong các loại cần thiết
            valid_prev = (
                self.prev_token is not None and
                self.prev_token.type in [
                    MiniGoLexer.ID, MiniGoLexer.KW_INT, MiniGoLexer.KW_FLOAT, MiniGoLexer.KW_STRING, 
                    MiniGoLexer.INT_LIT, MiniGoLexer.FLOAT_LIT, MiniGoLexer.STRING_LIT, MiniGoLexer.KW_NIL,
                    MiniGoLexer.RPAREN, MiniGoLexer.RBRACK, MiniGoLexer.RBRACE,
                    MiniGoLexer.KW_RETURN, MiniGoLexer.KW_CONTINUE, MiniGoLexer.KW_BREAK
                ]
            )
            if not valid_prev:
                return self.nextToken()

            # Nếu thỏa điều kiện, chuyển NEWLINE thành SEMI
            self.type = MiniGoLexer.SEMI
            self.text = ";"

        result = super().emit()
        self.prev_token = result
        return result


    def action(self, localctx:RuleContext, ruleIndex:int, actionIndex:int):
        if self._actions is None:
            actions = dict()
            actions[58] = self.UNCLOSE_STRING_action 
            actions[59] = self.ILLEGAL_ESCAPE_action 
            actions[64] = self.ERROR_CHAR_action 
            self._actions = actions
        action = self._actions.get(ruleIndex, None)
        if action is not None:
            action(localctx, actionIndex)
        else:
            raise Exception("No registered action for:" + str(ruleIndex))


    def UNCLOSE_STRING_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 0:

                if(len(self.text) >= 2 and self.text[-1] == '\n' and self.text[-2] == '\r'):
                    raise UncloseString(self.text[0:-2])
                elif (self.text[-1] == '\n'):
                    raise UncloseString(self.text[0:-1])
                else:
                    raise UncloseString(self.text[0:])

     

    def ILLEGAL_ESCAPE_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 1:

                raise IllegalEscape(self.text)

     

    def ERROR_CHAR_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 2:
             raise ErrorToken(self.text) 
     


