# Generated from main/minigo/parser/MiniGo.g4 by ANTLR 4.9.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3A")
        buf.write("\u0259\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23\t\23")
        buf.write("\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31")
        buf.write("\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36\t\36")
        buf.write("\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%\4&\t")
        buf.write("&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.\t.\4")
        buf.write("/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64\t\64")
        buf.write("\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\3\2\6\2r\n\2\r\2")
        buf.write("\16\2s\3\2\3\2\3\3\3\3\3\3\3\3\3\3\5\3}\n\3\3\4\3\4\3")
        buf.write("\5\3\5\3\5\3\5\3\5\5\5\u0086\n\5\3\5\3\5\5\5\u008a\n\5")
        buf.write("\3\5\3\5\3\6\3\6\3\6\3\6\3\6\3\6\3\7\3\7\3\7\3\7\5\7\u0098")
        buf.write("\n\7\3\7\3\7\5\7\u009c\n\7\3\7\5\7\u009f\n\7\3\7\3\7\3")
        buf.write("\b\3\b\3\b\7\b\u00a6\n\b\f\b\16\b\u00a9\13\b\3\t\3\t\3")
        buf.write("\t\3\n\3\n\3\n\7\n\u00b1\n\n\f\n\16\n\u00b4\13\n\3\13")
        buf.write("\3\13\6\13\u00b8\n\13\r\13\16\13\u00b9\3\13\3\13\3\f\3")
        buf.write("\f\3\f\3\f\3\f\3\f\3\f\3\f\3\f\5\f\u00c7\n\f\3\r\3\r\3")
        buf.write("\r\3\r\3\r\5\r\u00ce\n\r\3\r\3\r\5\r\u00d2\n\r\3\r\3\r")
        buf.write("\3\r\3\16\3\16\3\16\3\16\3\16\3\17\3\17\5\17\u00de\n\17")
        buf.write("\3\20\3\20\3\20\3\20\3\20\3\20\3\20\3\20\3\21\6\21\u00e9")
        buf.write("\n\21\r\21\16\21\u00ea\3\22\3\22\3\22\3\22\3\23\3\23\3")
        buf.write("\23\3\23\3\23\3\23\3\23\3\23\3\24\6\24\u00fa\n\24\r\24")
        buf.write("\16\24\u00fb\3\25\3\25\3\25\5\25\u0101\n\25\3\25\3\25")
        buf.write("\5\25\u0105\n\25\3\25\3\25\3\26\3\26\3\27\3\27\3\27\3")
        buf.write("\27\3\27\3\27\7\27\u0111\n\27\f\27\16\27\u0114\13\27\3")
        buf.write("\30\3\30\3\30\3\30\3\30\3\30\7\30\u011c\n\30\f\30\16\30")
        buf.write("\u011f\13\30\3\31\3\31\3\31\3\31\3\31\3\31\3\31\7\31\u0128")
        buf.write("\n\31\f\31\16\31\u012b\13\31\3\32\3\32\3\32\3\32\3\32")
        buf.write("\3\32\7\32\u0133\n\32\f\32\16\32\u0136\13\32\3\33\3\33")
        buf.write("\3\33\3\33\3\33\3\33\7\33\u013e\n\33\f\33\16\33\u0141")
        buf.write("\13\33\3\34\3\34\3\34\5\34\u0146\n\34\3\35\3\35\3\35\3")
        buf.write("\35\3\35\3\35\3\35\3\35\3\35\3\35\3\35\3\35\3\35\3\35")
        buf.write("\3\35\7\35\u0157\n\35\f\35\16\35\u015a\13\35\5\35\u015c")
        buf.write("\n\35\3\35\3\35\3\35\3\35\7\35\u0162\n\35\f\35\16\35\u0165")
        buf.write("\13\35\3\36\3\36\3\36\3\36\3\36\3\36\3\36\3\36\3\36\7")
        buf.write("\36\u0170\n\36\f\36\16\36\u0173\13\36\5\36\u0175\n\36")
        buf.write("\3\36\3\36\5\36\u0179\n\36\3\37\3\37\3\37\3\37\3\37\3")
        buf.write("\37\3\37\3\37\3\37\5\37\u0184\n\37\3 \3 \3 \3!\3!\3!\3")
        buf.write("!\7!\u018d\n!\f!\16!\u0190\13!\5!\u0192\n!\3!\3!\3\"\3")
        buf.write("\"\3\"\3\"\3#\3#\3#\3#\3#\3#\3#\3#\3#\3#\3#\7#\u01a5\n")
        buf.write("#\f#\16#\u01a8\13#\3$\3$\3%\3%\3%\3%\3%\3&\3&\5&\u01b3")
        buf.write("\n&\3&\3&\3\'\3\'\3\'\3\'\3\'\7\'\u01bc\n\'\f\'\16\'\u01bf")
        buf.write("\13\'\5\'\u01c1\n\'\3\'\3\'\3\'\3\'\3\'\3\'\3\'\3\'\3")
        buf.write("\'\7\'\u01cc\n\'\f\'\16\'\u01cf\13\'\5\'\u01d1\n\'\3\'")
        buf.write("\3\'\3\'\5\'\u01d6\n\'\3(\3(\3(\3)\3)\3)\3*\3*\3*\3*\3")
        buf.write("*\3*\7*\u01e4\n*\f*\16*\u01e7\13*\3*\5*\u01ea\n*\3*\3")
        buf.write("*\3+\3+\3+\3+\3+\3+\3+\3,\3,\3,\3-\3-\3.\3.\3.\3.\3.\5")
        buf.write(".\u01ff\n.\3.\3.\5.\u0203\n.\3/\3/\3\60\3\60\3\60\3\60")
        buf.write("\3\61\3\61\3\61\5\61\u020e\n\61\3\61\3\61\3\61\3\61\3")
        buf.write("\61\3\61\3\61\3\61\3\61\3\61\3\61\3\61\3\61\3\61\5\61")
        buf.write("\u021e\n\61\3\61\3\61\3\61\3\61\3\61\3\61\3\61\3\61\5")
        buf.write("\61\u0228\n\61\3\62\3\62\3\62\3\62\5\62\u022e\n\62\3\63")
        buf.write("\3\63\3\64\3\64\3\65\3\65\3\65\6\65\u0237\n\65\r\65\16")
        buf.write("\65\u0238\3\65\3\65\3\65\5\65\u023e\n\65\3\66\3\66\3\66")
        buf.write("\3\67\3\67\3\67\3\67\7\67\u0247\n\67\f\67\16\67\u024a")
        buf.write("\13\67\3\67\3\67\38\38\38\38\38\38\38\38\38\58\u0257\n")
        buf.write("8\38\2\t,.\60\62\648D9\2\4\6\b\n\f\16\20\22\24\26\30\32")
        buf.write("\34\36 \"$&(*,.\60\62\64\668:<>@BDFHJLNPRTVXZ\\^`bdfh")
        buf.write("jln\2\f\3\2\3\b\3\2\17\20\3\2\21\23\4\2\20\20\26\26\3")
        buf.write("\2\t\16\3\2+.\4\2\65\668;\4\2!!88\3\2)*\3\289\2\u0275")
        buf.write("\2q\3\2\2\2\4|\3\2\2\2\6~\3\2\2\2\b\u0080\3\2\2\2\n\u008d")
        buf.write("\3\2\2\2\f\u0093\3\2\2\2\16\u00a2\3\2\2\2\20\u00aa\3\2")
        buf.write("\2\2\22\u00ad\3\2\2\2\24\u00b5\3\2\2\2\26\u00c6\3\2\2")
        buf.write("\2\30\u00c8\3\2\2\2\32\u00d6\3\2\2\2\34\u00dd\3\2\2\2")
        buf.write("\36\u00df\3\2\2\2 \u00e8\3\2\2\2\"\u00ec\3\2\2\2$\u00f0")
        buf.write("\3\2\2\2&\u00f9\3\2\2\2(\u00fd\3\2\2\2*\u0108\3\2\2\2")
        buf.write(",\u010a\3\2\2\2.\u0115\3\2\2\2\60\u0120\3\2\2\2\62\u012c")
        buf.write("\3\2\2\2\64\u0137\3\2\2\2\66\u0145\3\2\2\28\u0147\3\2")
        buf.write("\2\2:\u0178\3\2\2\2<\u0183\3\2\2\2>\u0185\3\2\2\2@\u0188")
        buf.write("\3\2\2\2B\u0195\3\2\2\2D\u0199\3\2\2\2F\u01a9\3\2\2\2")
        buf.write("H\u01ab\3\2\2\2J\u01b0\3\2\2\2L\u01d5\3\2\2\2N\u01d7\3")
        buf.write("\2\2\2P\u01da\3\2\2\2R\u01dd\3\2\2\2T\u01ed\3\2\2\2V\u01f4")
        buf.write("\3\2\2\2X\u01f7\3\2\2\2Z\u01f9\3\2\2\2\\\u0204\3\2\2\2")
        buf.write("^\u0206\3\2\2\2`\u0227\3\2\2\2b\u022d\3\2\2\2d\u022f\3")
        buf.write("\2\2\2f\u0231\3\2\2\2h\u0236\3\2\2\2j\u023f\3\2\2\2l\u0242")
        buf.write("\3\2\2\2n\u0256\3\2\2\2pr\5\4\3\2qp\3\2\2\2rs\3\2\2\2")
        buf.write("sq\3\2\2\2st\3\2\2\2tu\3\2\2\2uv\7\2\2\3v\3\3\2\2\2w}")
        buf.write("\5\n\6\2x}\5\b\5\2y}\5\f\7\2z}\5\30\r\2{}\5\34\17\2|w")
        buf.write("\3\2\2\2|x\3\2\2\2|y\3\2\2\2|z\3\2\2\2|{\3\2\2\2}\5\3")
        buf.write("\2\2\2~\177\5b\62\2\177\7\3\2\2\2\u0080\u0081\7\60\2\2")
        buf.write("\u0081\u0089\78\2\2\u0082\u0085\5b\62\2\u0083\u0084\7")
        buf.write("\27\2\2\u0084\u0086\5,\27\2\u0085\u0083\3\2\2\2\u0085")
        buf.write("\u0086\3\2\2\2\u0086\u008a\3\2\2\2\u0087\u0088\7\27\2")
        buf.write("\2\u0088\u008a\5,\27\2\u0089\u0082\3\2\2\2\u0089\u0087")
        buf.write("\3\2\2\2\u008a\u008b\3\2\2\2\u008b\u008c\7\31\2\2\u008c")
        buf.write("\t\3\2\2\2\u008d\u008e\7/\2\2\u008e\u008f\78\2\2\u008f")
        buf.write("\u0090\7\27\2\2\u0090\u0091\5,\27\2\u0091\u0092\7\31\2")
        buf.write("\2\u0092\13\3\2\2\2\u0093\u0094\7\'\2\2\u0094\u0095\7")
        buf.write("8\2\2\u0095\u0097\7\32\2\2\u0096\u0098\5\16\b\2\u0097")
        buf.write("\u0096\3\2\2\2\u0097\u0098\3\2\2\2\u0098\u0099\3\2\2\2")
        buf.write("\u0099\u009b\7\33\2\2\u009a\u009c\5\6\4\2\u009b\u009a")
        buf.write("\3\2\2\2\u009b\u009c\3\2\2\2\u009c\u009e\3\2\2\2\u009d")
        buf.write("\u009f\5\24\13\2\u009e\u009d\3\2\2\2\u009e\u009f\3\2\2")
        buf.write("\2\u009f\u00a0\3\2\2\2\u00a0\u00a1\7\31\2\2\u00a1\r\3")
        buf.write("\2\2\2\u00a2\u00a7\5\20\t\2\u00a3\u00a4\7 \2\2\u00a4\u00a6")
        buf.write("\5\20\t\2\u00a5\u00a3\3\2\2\2\u00a6\u00a9\3\2\2\2\u00a7")
        buf.write("\u00a5\3\2\2\2\u00a7\u00a8\3\2\2\2\u00a8\17\3\2\2\2\u00a9")
        buf.write("\u00a7\3\2\2\2\u00aa\u00ab\5\22\n\2\u00ab\u00ac\5b\62")
        buf.write("\2\u00ac\21\3\2\2\2\u00ad\u00b2\78\2\2\u00ae\u00af\7 ")
        buf.write("\2\2\u00af\u00b1\78\2\2\u00b0\u00ae\3\2\2\2\u00b1\u00b4")
        buf.write("\3\2\2\2\u00b2\u00b0\3\2\2\2\u00b2\u00b3\3\2\2\2\u00b3")
        buf.write("\23\3\2\2\2\u00b4\u00b2\3\2\2\2\u00b5\u00b7\7\36\2\2\u00b6")
        buf.write("\u00b8\5\26\f\2\u00b7\u00b6\3\2\2\2\u00b8\u00b9\3\2\2")
        buf.write("\2\u00b9\u00b7\3\2\2\2\u00b9\u00ba\3\2\2\2\u00ba\u00bb")
        buf.write("\3\2\2\2\u00bb\u00bc\7\37\2\2\u00bc\25\3\2\2\2\u00bd\u00c7")
        buf.write("\5L\'\2\u00be\u00c7\5\n\6\2\u00bf\u00c7\5\b\5\2\u00c0")
        buf.write("\u00c7\5R*\2\u00c1\u00c7\5`\61\2\u00c2\u00c7\5J&\2\u00c3")
        buf.write("\u00c7\5H%\2\u00c4\u00c7\5N(\2\u00c5\u00c7\5P)\2\u00c6")
        buf.write("\u00bd\3\2\2\2\u00c6\u00be\3\2\2\2\u00c6\u00bf\3\2\2\2")
        buf.write("\u00c6\u00c0\3\2\2\2\u00c6\u00c1\3\2\2\2\u00c6\u00c2\3")
        buf.write("\2\2\2\u00c6\u00c3\3\2\2\2\u00c6\u00c4\3\2\2\2\u00c6\u00c5")
        buf.write("\3\2\2\2\u00c7\27\3\2\2\2\u00c8\u00c9\7\'\2\2\u00c9\u00ca")
        buf.write("\5\32\16\2\u00ca\u00cb\78\2\2\u00cb\u00cd\7\32\2\2\u00cc")
        buf.write("\u00ce\5\16\b\2\u00cd\u00cc\3\2\2\2\u00cd\u00ce\3\2\2")
        buf.write("\2\u00ce\u00cf\3\2\2\2\u00cf\u00d1\7\33\2\2\u00d0\u00d2")
        buf.write("\5\6\4\2\u00d1\u00d0\3\2\2\2\u00d1\u00d2\3\2\2\2\u00d2")
        buf.write("\u00d3\3\2\2\2\u00d3\u00d4\5\24\13\2\u00d4\u00d5\7\31")
        buf.write("\2\2\u00d5\31\3\2\2\2\u00d6\u00d7\7\32\2\2\u00d7\u00d8")
        buf.write("\78\2\2\u00d8\u00d9\78\2\2\u00d9\u00da\7\33\2\2\u00da")
        buf.write("\33\3\2\2\2\u00db\u00de\5\36\20\2\u00dc\u00de\5$\23\2")
        buf.write("\u00dd\u00db\3\2\2\2\u00dd\u00dc\3\2\2\2\u00de\35\3\2")
        buf.write("\2\2\u00df\u00e0\7(\2\2\u00e0\u00e1\78\2\2\u00e1\u00e2")
        buf.write("\7)\2\2\u00e2\u00e3\7\36\2\2\u00e3\u00e4\5 \21\2\u00e4")
        buf.write("\u00e5\7\37\2\2\u00e5\u00e6\7\31\2\2\u00e6\37\3\2\2\2")
        buf.write("\u00e7\u00e9\5\"\22\2\u00e8\u00e7\3\2\2\2\u00e9\u00ea")
        buf.write("\3\2\2\2\u00ea\u00e8\3\2\2\2\u00ea\u00eb\3\2\2\2\u00eb")
        buf.write("!\3\2\2\2\u00ec\u00ed\78\2\2\u00ed\u00ee\5b\62\2\u00ee")
        buf.write("\u00ef\7\31\2\2\u00ef#\3\2\2\2\u00f0\u00f1\7(\2\2\u00f1")
        buf.write("\u00f2\78\2\2\u00f2\u00f3\7*\2\2\u00f3\u00f4\7\36\2\2")
        buf.write("\u00f4\u00f5\5&\24\2\u00f5\u00f6\7\37\2\2\u00f6\u00f7")
        buf.write("\7\31\2\2\u00f7%\3\2\2\2\u00f8\u00fa\5(\25\2\u00f9\u00f8")
        buf.write("\3\2\2\2\u00fa\u00fb\3\2\2\2\u00fb\u00f9\3\2\2\2\u00fb")
        buf.write("\u00fc\3\2\2\2\u00fc\'\3\2\2\2\u00fd\u00fe\78\2\2\u00fe")
        buf.write("\u0100\7\32\2\2\u00ff\u0101\5\16\b\2\u0100\u00ff\3\2\2")
        buf.write("\2\u0100\u0101\3\2\2\2\u0101\u0102\3\2\2\2\u0102\u0104")
        buf.write("\7\33\2\2\u0103\u0105\5\6\4\2\u0104\u0103\3\2\2\2\u0104")
        buf.write("\u0105\3\2\2\2\u0105\u0106\3\2\2\2\u0106\u0107\7\31\2")
        buf.write("\2\u0107)\3\2\2\2\u0108\u0109\t\2\2\2\u0109+\3\2\2\2\u010a")
        buf.write("\u010b\b\27\1\2\u010b\u010c\5.\30\2\u010c\u0112\3\2\2")
        buf.write("\2\u010d\u010e\f\4\2\2\u010e\u010f\7\25\2\2\u010f\u0111")
        buf.write("\5.\30\2\u0110\u010d\3\2\2\2\u0111\u0114\3\2\2\2\u0112")
        buf.write("\u0110\3\2\2\2\u0112\u0113\3\2\2\2\u0113-\3\2\2\2\u0114")
        buf.write("\u0112\3\2\2\2\u0115\u0116\b\30\1\2\u0116\u0117\5\60\31")
        buf.write("\2\u0117\u011d\3\2\2\2\u0118\u0119\f\4\2\2\u0119\u011a")
        buf.write("\7\24\2\2\u011a\u011c\5\60\31\2\u011b\u0118\3\2\2\2\u011c")
        buf.write("\u011f\3\2\2\2\u011d\u011b\3\2\2\2\u011d\u011e\3\2\2\2")
        buf.write("\u011e/\3\2\2\2\u011f\u011d\3\2\2\2\u0120\u0121\b\31\1")
        buf.write("\2\u0121\u0122\5\62\32\2\u0122\u0129\3\2\2\2\u0123\u0124")
        buf.write("\f\4\2\2\u0124\u0125\5*\26\2\u0125\u0126\5\62\32\2\u0126")
        buf.write("\u0128\3\2\2\2\u0127\u0123\3\2\2\2\u0128\u012b\3\2\2\2")
        buf.write("\u0129\u0127\3\2\2\2\u0129\u012a\3\2\2\2\u012a\61\3\2")
        buf.write("\2\2\u012b\u0129\3\2\2\2\u012c\u012d\b\32\1\2\u012d\u012e")
        buf.write("\5\64\33\2\u012e\u0134\3\2\2\2\u012f\u0130\f\4\2\2\u0130")
        buf.write("\u0131\t\3\2\2\u0131\u0133\5\64\33\2\u0132\u012f\3\2\2")
        buf.write("\2\u0133\u0136\3\2\2\2\u0134\u0132\3\2\2\2\u0134\u0135")
        buf.write("\3\2\2\2\u0135\63\3\2\2\2\u0136\u0134\3\2\2\2\u0137\u0138")
        buf.write("\b\33\1\2\u0138\u0139\5\66\34\2\u0139\u013f\3\2\2\2\u013a")
        buf.write("\u013b\f\4\2\2\u013b\u013c\t\4\2\2\u013c\u013e\5\66\34")
        buf.write("\2\u013d\u013a\3\2\2\2\u013e\u0141\3\2\2\2\u013f\u013d")
        buf.write("\3\2\2\2\u013f\u0140\3\2\2\2\u0140\65\3\2\2\2\u0141\u013f")
        buf.write("\3\2\2\2\u0142\u0143\t\5\2\2\u0143\u0146\5\66\34\2\u0144")
        buf.write("\u0146\58\35\2\u0145\u0142\3\2\2\2\u0145\u0144\3\2\2\2")
        buf.write("\u0146\67\3\2\2\2\u0147\u0148\b\35\1\2\u0148\u0149\5:")
        buf.write("\36\2\u0149\u0163\3\2\2\2\u014a\u014b\f\6\2\2\u014b\u014c")
        buf.write("\7\34\2\2\u014c\u014d\5,\27\2\u014d\u014e\7\35\2\2\u014e")
        buf.write("\u0162\3\2\2\2\u014f\u0150\f\5\2\2\u0150\u0151\7\30\2")
        buf.write("\2\u0151\u0152\78\2\2\u0152\u015b\7\32\2\2\u0153\u0158")
        buf.write("\5,\27\2\u0154\u0155\7 \2\2\u0155\u0157\5,\27\2\u0156")
        buf.write("\u0154\3\2\2\2\u0157\u015a\3\2\2\2\u0158\u0156\3\2\2\2")
        buf.write("\u0158\u0159\3\2\2\2\u0159\u015c\3\2\2\2\u015a\u0158\3")
        buf.write("\2\2\2\u015b\u0153\3\2\2\2\u015b\u015c\3\2\2\2\u015c\u015d")
        buf.write("\3\2\2\2\u015d\u0162\7\33\2\2\u015e\u015f\f\4\2\2\u015f")
        buf.write("\u0160\7\30\2\2\u0160\u0162\78\2\2\u0161\u014a\3\2\2\2")
        buf.write("\u0161\u014f\3\2\2\2\u0161\u015e\3\2\2\2\u0162\u0165\3")
        buf.write("\2\2\2\u0163\u0161\3\2\2\2\u0163\u0164\3\2\2\2\u01649")
        buf.write("\3\2\2\2\u0165\u0163\3\2\2\2\u0166\u0167\7\32\2\2\u0167")
        buf.write("\u0168\5,\27\2\u0168\u0169\7\33\2\2\u0169\u0179\3\2\2")
        buf.write("\2\u016a\u016b\78\2\2\u016b\u0174\7\32\2\2\u016c\u0171")
        buf.write("\5,\27\2\u016d\u016e\7 \2\2\u016e\u0170\5,\27\2\u016f")
        buf.write("\u016d\3\2\2\2\u0170\u0173\3\2\2\2\u0171\u016f\3\2\2\2")
        buf.write("\u0171\u0172\3\2\2\2\u0172\u0175\3\2\2\2\u0173\u0171\3")
        buf.write("\2\2\2\u0174\u016c\3\2\2\2\u0174\u0175\3\2\2\2\u0175\u0176")
        buf.write("\3\2\2\2\u0176\u0179\7\33\2\2\u0177\u0179\5<\37\2\u0178")
        buf.write("\u0166\3\2\2\2\u0178\u016a\3\2\2\2\u0178\u0177\3\2\2\2")
        buf.write("\u0179;\3\2\2\2\u017a\u0184\78\2\2\u017b\u0184\79\2\2")
        buf.write("\u017c\u0184\7:\2\2\u017d\u0184\7;\2\2\u017e\u0184\5j")
        buf.write("\66\2\u017f\u0184\5> \2\u0180\u0184\7\65\2\2\u0181\u0184")
        buf.write("\7\66\2\2\u0182\u0184\7\64\2\2\u0183\u017a\3\2\2\2\u0183")
        buf.write("\u017b\3\2\2\2\u0183\u017c\3\2\2\2\u0183\u017d\3\2\2\2")
        buf.write("\u0183\u017e\3\2\2\2\u0183\u017f\3\2\2\2\u0183\u0180\3")
        buf.write("\2\2\2\u0183\u0181\3\2\2\2\u0183\u0182\3\2\2\2\u0184=")
        buf.write("\3\2\2\2\u0185\u0186\78\2\2\u0186\u0187\5@!\2\u0187?\3")
        buf.write("\2\2\2\u0188\u0191\7\36\2\2\u0189\u018e\5B\"\2\u018a\u018b")
        buf.write("\7 \2\2\u018b\u018d\5B\"\2\u018c\u018a\3\2\2\2\u018d\u0190")
        buf.write("\3\2\2\2\u018e\u018c\3\2\2\2\u018e\u018f\3\2\2\2\u018f")
        buf.write("\u0192\3\2\2\2\u0190\u018e\3\2\2\2\u0191\u0189\3\2\2\2")
        buf.write("\u0191\u0192\3\2\2\2\u0192\u0193\3\2\2\2\u0193\u0194\7")
        buf.write("\37\2\2\u0194A\3\2\2\2\u0195\u0196\78\2\2\u0196\u0197")
        buf.write("\7\"\2\2\u0197\u0198\5,\27\2\u0198C\3\2\2\2\u0199\u019a")
        buf.write("\b#\1\2\u019a\u019b\78\2\2\u019b\u01a6\3\2\2\2\u019c\u019d")
        buf.write("\f\4\2\2\u019d\u019e\7\34\2\2\u019e\u019f\5,\27\2\u019f")
        buf.write("\u01a0\7\35\2\2\u01a0\u01a5\3\2\2\2\u01a1\u01a2\f\3\2")
        buf.write("\2\u01a2\u01a3\7\30\2\2\u01a3\u01a5\78\2\2\u01a4\u019c")
        buf.write("\3\2\2\2\u01a4\u01a1\3\2\2\2\u01a5\u01a8\3\2\2\2\u01a6")
        buf.write("\u01a4\3\2\2\2\u01a6\u01a7\3\2\2\2\u01a7E\3\2\2\2\u01a8")
        buf.write("\u01a6\3\2\2\2\u01a9\u01aa\t\6\2\2\u01aaG\3\2\2\2\u01ab")
        buf.write("\u01ac\5D#\2\u01ac\u01ad\5F$\2\u01ad\u01ae\5,\27\2\u01ae")
        buf.write("\u01af\7\31\2\2\u01afI\3\2\2\2\u01b0\u01b2\7&\2\2\u01b1")
        buf.write("\u01b3\5,\27\2\u01b2\u01b1\3\2\2\2\u01b2\u01b3\3\2\2\2")
        buf.write("\u01b3\u01b4\3\2\2\2\u01b4\u01b5\7\31\2\2\u01b5K\3\2\2")
        buf.write("\2\u01b6\u01b7\78\2\2\u01b7\u01c0\7\32\2\2\u01b8\u01bd")
        buf.write("\5,\27\2\u01b9\u01ba\7 \2\2\u01ba\u01bc\5,\27\2\u01bb")
        buf.write("\u01b9\3\2\2\2\u01bc\u01bf\3\2\2\2\u01bd\u01bb\3\2\2\2")
        buf.write("\u01bd\u01be\3\2\2\2\u01be\u01c1\3\2\2\2\u01bf\u01bd\3")
        buf.write("\2\2\2\u01c0\u01b8\3\2\2\2\u01c0\u01c1\3\2\2\2\u01c1\u01c2")
        buf.write("\3\2\2\2\u01c2\u01c3\7\33\2\2\u01c3\u01d6\7\31\2\2\u01c4")
        buf.write("\u01c5\5,\27\2\u01c5\u01c6\7\30\2\2\u01c6\u01c7\78\2\2")
        buf.write("\u01c7\u01d0\7\32\2\2\u01c8\u01cd\5,\27\2\u01c9\u01ca")
        buf.write("\7 \2\2\u01ca\u01cc\5,\27\2\u01cb\u01c9\3\2\2\2\u01cc")
        buf.write("\u01cf\3\2\2\2\u01cd\u01cb\3\2\2\2\u01cd\u01ce\3\2\2\2")
        buf.write("\u01ce\u01d1\3\2\2\2\u01cf\u01cd\3\2\2\2\u01d0\u01c8\3")
        buf.write("\2\2\2\u01d0\u01d1\3\2\2\2\u01d1\u01d2\3\2\2\2\u01d2\u01d3")
        buf.write("\7\33\2\2\u01d3\u01d4\7\31\2\2\u01d4\u01d6\3\2\2\2\u01d5")
        buf.write("\u01b6\3\2\2\2\u01d5\u01c4\3\2\2\2\u01d6M\3\2\2\2\u01d7")
        buf.write("\u01d8\7\62\2\2\u01d8\u01d9\7\31\2\2\u01d9O\3\2\2\2\u01da")
        buf.write("\u01db\7\61\2\2\u01db\u01dc\7\31\2\2\u01dcQ\3\2\2\2\u01dd")
        buf.write("\u01de\7#\2\2\u01de\u01df\7\32\2\2\u01df\u01e0\5,\27\2")
        buf.write("\u01e0\u01e1\7\33\2\2\u01e1\u01e5\5\24\13\2\u01e2\u01e4")
        buf.write("\5T+\2\u01e3\u01e2\3\2\2\2\u01e4\u01e7\3\2\2\2\u01e5\u01e3")
        buf.write("\3\2\2\2\u01e5\u01e6\3\2\2\2\u01e6\u01e9\3\2\2\2\u01e7")
        buf.write("\u01e5\3\2\2\2\u01e8\u01ea\5V,\2\u01e9\u01e8\3\2\2\2\u01e9")
        buf.write("\u01ea\3\2\2\2\u01ea\u01eb\3\2\2\2\u01eb\u01ec\7\31\2")
        buf.write("\2\u01ecS\3\2\2\2\u01ed\u01ee\7$\2\2\u01ee\u01ef\7#\2")
        buf.write("\2\u01ef\u01f0\7\32\2\2\u01f0\u01f1\5,\27\2\u01f1\u01f2")
        buf.write("\7\33\2\2\u01f2\u01f3\5\24\13\2\u01f3U\3\2\2\2\u01f4\u01f5")
        buf.write("\7$\2\2\u01f5\u01f6\5\24\13\2\u01f6W\3\2\2\2\u01f7\u01f8")
        buf.write("\t\7\2\2\u01f8Y\3\2\2\2\u01f9\u01fa\7\60\2\2\u01fa\u0202")
        buf.write("\78\2\2\u01fb\u01fe\5X-\2\u01fc\u01fd\7\27\2\2\u01fd\u01ff")
        buf.write("\5,\27\2\u01fe\u01fc\3\2\2\2\u01fe\u01ff\3\2\2\2\u01ff")
        buf.write("\u0203\3\2\2\2\u0200\u0201\7\27\2\2\u0201\u0203\5,\27")
        buf.write("\2\u0202\u01fb\3\2\2\2\u0202\u0200\3\2\2\2\u0203[\3\2")
        buf.write("\2\2\u0204\u0205\t\b\2\2\u0205]\3\2\2\2\u0206\u0207\5")
        buf.write("\\/\2\u0207\u0208\5F$\2\u0208\u0209\5,\27\2\u0209_\3\2")
        buf.write("\2\2\u020a\u020d\7%\2\2\u020b\u020e\5Z.\2\u020c\u020e")
        buf.write("\5^\60\2\u020d\u020b\3\2\2\2\u020d\u020c\3\2\2\2\u020e")
        buf.write("\u020f\3\2\2\2\u020f\u0210\7\31\2\2\u0210\u0211\5,\27")
        buf.write("\2\u0211\u0212\7\31\2\2\u0212\u0213\5^\60\2\u0213\u0214")
        buf.write("\5\24\13\2\u0214\u0215\7\31\2\2\u0215\u0228\3\2\2\2\u0216")
        buf.write("\u0217\7%\2\2\u0217\u0218\5,\27\2\u0218\u0219\5\24\13")
        buf.write("\2\u0219\u021a\7\31\2\2\u021a\u0228\3\2\2\2\u021b\u021d")
        buf.write("\7%\2\2\u021c\u021e\t\t\2\2\u021d\u021c\3\2\2\2\u021d")
        buf.write("\u021e\3\2\2\2\u021e\u021f\3\2\2\2\u021f\u0220\7 \2\2")
        buf.write("\u0220\u0221\78\2\2\u0221\u0222\7\t\2\2\u0222\u0223\7")
        buf.write("\63\2\2\u0223\u0224\5,\27\2\u0224\u0225\5\24\13\2\u0225")
        buf.write("\u0226\7\31\2\2\u0226\u0228\3\2\2\2\u0227\u020a\3\2\2")
        buf.write("\2\u0227\u0216\3\2\2\2\u0227\u021b\3\2\2\2\u0228a\3\2")
        buf.write("\2\2\u0229\u022e\5h\65\2\u022a\u022e\5d\63\2\u022b\u022e")
        buf.write("\5f\64\2\u022c\u022e\78\2\2\u022d\u0229\3\2\2\2\u022d")
        buf.write("\u022a\3\2\2\2\u022d\u022b\3\2\2\2\u022d\u022c\3\2\2\2")
        buf.write("\u022ec\3\2\2\2\u022f\u0230\t\7\2\2\u0230e\3\2\2\2\u0231")
        buf.write("\u0232\t\n\2\2\u0232g\3\2\2\2\u0233\u0234\7\34\2\2\u0234")
        buf.write("\u0235\t\13\2\2\u0235\u0237\7\35\2\2\u0236\u0233\3\2\2")
        buf.write("\2\u0237\u0238\3\2\2\2\u0238\u0236\3\2\2\2\u0238\u0239")
        buf.write("\3\2\2\2\u0239\u023d\3\2\2\2\u023a\u023e\5d\63\2\u023b")
        buf.write("\u023e\5f\64\2\u023c\u023e\78\2\2\u023d\u023a\3\2\2\2")
        buf.write("\u023d\u023b\3\2\2\2\u023d\u023c\3\2\2\2\u023ei\3\2\2")
        buf.write("\2\u023f\u0240\5h\65\2\u0240\u0241\5l\67\2\u0241k\3\2")
        buf.write("\2\2\u0242\u0243\7\36\2\2\u0243\u0248\5n8\2\u0244\u0245")
        buf.write("\7 \2\2\u0245\u0247\5n8\2\u0246\u0244\3\2\2\2\u0247\u024a")
        buf.write("\3\2\2\2\u0248\u0246\3\2\2\2\u0248\u0249\3\2\2\2\u0249")
        buf.write("\u024b\3\2\2\2\u024a\u0248\3\2\2\2\u024b\u024c\7\37\2")
        buf.write("\2\u024cm\3\2\2\2\u024d\u0257\78\2\2\u024e\u0257\79\2")
        buf.write("\2\u024f\u0257\7:\2\2\u0250\u0257\7\65\2\2\u0251\u0257")
        buf.write("\7\66\2\2\u0252\u0257\7\64\2\2\u0253\u0257\7;\2\2\u0254")
        buf.write("\u0257\5> \2\u0255\u0257\5l\67\2\u0256\u024d\3\2\2\2\u0256")
        buf.write("\u024e\3\2\2\2\u0256\u024f\3\2\2\2\u0256\u0250\3\2\2\2")
        buf.write("\u0256\u0251\3\2\2\2\u0256\u0252\3\2\2\2\u0256\u0253\3")
        buf.write("\2\2\2\u0256\u0254\3\2\2\2\u0256\u0255\3\2\2\2\u0257o")
        buf.write("\3\2\2\28s|\u0085\u0089\u0097\u009b\u009e\u00a7\u00b2")
        buf.write("\u00b9\u00c6\u00cd\u00d1\u00dd\u00ea\u00fb\u0100\u0104")
        buf.write("\u0112\u011d\u0129\u0134\u013f\u0145\u0158\u015b\u0161")
        buf.write("\u0163\u0171\u0174\u0178\u0183\u018e\u0191\u01a4\u01a6")
        buf.write("\u01b2\u01bd\u01c0\u01cd\u01d0\u01d5\u01e5\u01e9\u01fe")
        buf.write("\u0202\u020d\u021d\u0227\u022d\u0238\u023d\u0248\u0256")
        return buf.getvalue()


class MiniGoParser ( Parser ):

    grammarFileName = "MiniGo.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'=='", "'!='", "'<'", "'<='", "'>'", 
                     "'>='", "':='", "'+='", "'-='", "'*='", "'/='", "'%='", 
                     "'+'", "'-'", "'*'", "'/'", "'%'", "'&&'", "'||'", 
                     "'!'", "'='", "'.'", "';'", "'('", "')'", "'['", "']'", 
                     "'{'", "'}'", "','", "'_'", "':'", "'if'", "'else'", 
                     "'for'", "'return'", "'func'", "'type'", "'struct'", 
                     "'interface'", "'string'", "'int'", "'float'", "'boolean'", 
                     "'const'", "'var'", "'continue'", "'break'", "'range'", 
                     "'nil'", "'true'", "'false'" ]

    symbolicNames = [ "<INVALID>", "EQ", "NEQ", "LT", "LE", "GT", "GE", 
                      "ASSIGN_INIT", "ADD_ASSIGN", "SUB_ASSIGN", "MUL_ASSIGN", 
                      "DIV_ASSIGN", "MOD_ASSIGN", "PLUS", "MINUS", "MULT", 
                      "DIV", "MOD", "AND", "OR", "NOT", "ASSIGN", "DOT", 
                      "SEMI", "LPAREN", "RPAREN", "LBRACK", "RBRACK", "LBRACE", 
                      "RBRACE", "COMMA", "UNDERSCORE", "COLON", "KW_IF", 
                      "KW_ELSE", "KW_FOR", "KW_RETURN", "KW_FUNC", "KW_TYPE", 
                      "KW_STRUCT", "KW_INTERFACE", "KW_STRING", "KW_INT", 
                      "KW_FLOAT", "KW_BOOLEAN", "KW_CONST", "KW_VAR", "KW_CONTINUE", 
                      "KW_BREAK", "KW_RANGE", "KW_NIL", "KW_TRUE", "KW_FALSE", 
                      "NEWLINE", "ID", "INT_LIT", "FLOAT_LIT", "STRING_LIT", 
                      "UNCLOSE_STRING", "ILLEGAL_ESCAPE", "WS", "COMMENT", 
                      "MULTILINE_COMMENT", "ERROR_CHAR" ]

    RULE_program = 0
    RULE_decl = 1
    RULE_returntype = 2
    RULE_vardecl = 3
    RULE_constdecl = 4
    RULE_funcdecl = 5
    RULE_paramlist = 6
    RULE_param = 7
    RULE_identifierList = 8
    RULE_block = 9
    RULE_stmt = 10
    RULE_methoddecl = 11
    RULE_receiver = 12
    RULE_typedef = 13
    RULE_structType = 14
    RULE_structfields = 15
    RULE_fielddecl = 16
    RULE_interfaceType = 17
    RULE_interfaceMethodList = 18
    RULE_interfaceMethodDecl = 19
    RULE_compare = 20
    RULE_expr = 21
    RULE_expr1 = 22
    RULE_expr2 = 23
    RULE_expr3 = 24
    RULE_expr4 = 25
    RULE_expr5 = 26
    RULE_expr6 = 27
    RULE_expr7 = 28
    RULE_term = 29
    RULE_structliteral = 30
    RULE_structliteralbody = 31
    RULE_fieldinit = 32
    RULE_lvalue = 33
    RULE_assign_op = 34
    RULE_assignstmt = 35
    RULE_returnstmt = 36
    RULE_callstmt = 37
    RULE_breakstmt = 38
    RULE_continuestmt = 39
    RULE_ifstmt = 40
    RULE_elseifstmt = 41
    RULE_elsestmt = 42
    RULE_datatypefor = 43
    RULE_vardeclfor = 44
    RULE_lvaluefor = 45
    RULE_assignstmtforscalar = 46
    RULE_forstmt = 47
    RULE_datatype = 48
    RULE_primitive_type = 49
    RULE_composite_type = 50
    RULE_arraytype = 51
    RULE_arrayliteral = 52
    RULE_literalbody = 53
    RULE_arrayelement = 54

    ruleNames =  [ "program", "decl", "returntype", "vardecl", "constdecl", 
                   "funcdecl", "paramlist", "param", "identifierList", "block", 
                   "stmt", "methoddecl", "receiver", "typedef", "structType", 
                   "structfields", "fielddecl", "interfaceType", "interfaceMethodList", 
                   "interfaceMethodDecl", "compare", "expr", "expr1", "expr2", 
                   "expr3", "expr4", "expr5", "expr6", "expr7", "term", 
                   "structliteral", "structliteralbody", "fieldinit", "lvalue", 
                   "assign_op", "assignstmt", "returnstmt", "callstmt", 
                   "breakstmt", "continuestmt", "ifstmt", "elseifstmt", 
                   "elsestmt", "datatypefor", "vardeclfor", "lvaluefor", 
                   "assignstmtforscalar", "forstmt", "datatype", "primitive_type", 
                   "composite_type", "arraytype", "arrayliteral", "literalbody", 
                   "arrayelement" ]

    EOF = Token.EOF
    EQ=1
    NEQ=2
    LT=3
    LE=4
    GT=5
    GE=6
    ASSIGN_INIT=7
    ADD_ASSIGN=8
    SUB_ASSIGN=9
    MUL_ASSIGN=10
    DIV_ASSIGN=11
    MOD_ASSIGN=12
    PLUS=13
    MINUS=14
    MULT=15
    DIV=16
    MOD=17
    AND=18
    OR=19
    NOT=20
    ASSIGN=21
    DOT=22
    SEMI=23
    LPAREN=24
    RPAREN=25
    LBRACK=26
    RBRACK=27
    LBRACE=28
    RBRACE=29
    COMMA=30
    UNDERSCORE=31
    COLON=32
    KW_IF=33
    KW_ELSE=34
    KW_FOR=35
    KW_RETURN=36
    KW_FUNC=37
    KW_TYPE=38
    KW_STRUCT=39
    KW_INTERFACE=40
    KW_STRING=41
    KW_INT=42
    KW_FLOAT=43
    KW_BOOLEAN=44
    KW_CONST=45
    KW_VAR=46
    KW_CONTINUE=47
    KW_BREAK=48
    KW_RANGE=49
    KW_NIL=50
    KW_TRUE=51
    KW_FALSE=52
    NEWLINE=53
    ID=54
    INT_LIT=55
    FLOAT_LIT=56
    STRING_LIT=57
    UNCLOSE_STRING=58
    ILLEGAL_ESCAPE=59
    WS=60
    COMMENT=61
    MULTILINE_COMMENT=62
    ERROR_CHAR=63

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(MiniGoParser.EOF, 0)

        def decl(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniGoParser.DeclContext)
            else:
                return self.getTypedRuleContext(MiniGoParser.DeclContext,i)


        def getRuleIndex(self):
            return MiniGoParser.RULE_program

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProgram" ):
                return visitor.visitProgram(self)
            else:
                return visitor.visitChildren(self)




    def program(self):

        localctx = MiniGoParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 111 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 110
                self.decl()
                self.state = 113 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.KW_FUNC) | (1 << MiniGoParser.KW_TYPE) | (1 << MiniGoParser.KW_CONST) | (1 << MiniGoParser.KW_VAR))) != 0)):
                    break

            self.state = 115
            self.match(MiniGoParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def constdecl(self):
            return self.getTypedRuleContext(MiniGoParser.ConstdeclContext,0)


        def vardecl(self):
            return self.getTypedRuleContext(MiniGoParser.VardeclContext,0)


        def funcdecl(self):
            return self.getTypedRuleContext(MiniGoParser.FuncdeclContext,0)


        def methoddecl(self):
            return self.getTypedRuleContext(MiniGoParser.MethoddeclContext,0)


        def typedef(self):
            return self.getTypedRuleContext(MiniGoParser.TypedefContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_decl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDecl" ):
                return visitor.visitDecl(self)
            else:
                return visitor.visitChildren(self)




    def decl(self):

        localctx = MiniGoParser.DeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_decl)
        try:
            self.state = 122
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 117
                self.constdecl()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 118
                self.vardecl()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 119
                self.funcdecl()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 120
                self.methoddecl()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 121
                self.typedef()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ReturntypeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def datatype(self):
            return self.getTypedRuleContext(MiniGoParser.DatatypeContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_returntype

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitReturntype" ):
                return visitor.visitReturntype(self)
            else:
                return visitor.visitChildren(self)




    def returntype(self):

        localctx = MiniGoParser.ReturntypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_returntype)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 124
            self.datatype()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VardeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def KW_VAR(self):
            return self.getToken(MiniGoParser.KW_VAR, 0)

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def SEMI(self):
            return self.getToken(MiniGoParser.SEMI, 0)

        def datatype(self):
            return self.getTypedRuleContext(MiniGoParser.DatatypeContext,0)


        def ASSIGN(self):
            return self.getToken(MiniGoParser.ASSIGN, 0)

        def expr(self):
            return self.getTypedRuleContext(MiniGoParser.ExprContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_vardecl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVardecl" ):
                return visitor.visitVardecl(self)
            else:
                return visitor.visitChildren(self)




    def vardecl(self):

        localctx = MiniGoParser.VardeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_vardecl)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 126
            self.match(MiniGoParser.KW_VAR)
            self.state = 127
            self.match(MiniGoParser.ID)
            self.state = 135
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.LBRACK, MiniGoParser.KW_STRUCT, MiniGoParser.KW_INTERFACE, MiniGoParser.KW_STRING, MiniGoParser.KW_INT, MiniGoParser.KW_FLOAT, MiniGoParser.KW_BOOLEAN, MiniGoParser.ID]:
                self.state = 128
                self.datatype()
                self.state = 131
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==MiniGoParser.ASSIGN:
                    self.state = 129
                    self.match(MiniGoParser.ASSIGN)
                    self.state = 130
                    self.expr(0)


                pass
            elif token in [MiniGoParser.ASSIGN]:
                self.state = 133
                self.match(MiniGoParser.ASSIGN)
                self.state = 134
                self.expr(0)
                pass
            else:
                raise NoViableAltException(self)

            self.state = 137
            self.match(MiniGoParser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ConstdeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def KW_CONST(self):
            return self.getToken(MiniGoParser.KW_CONST, 0)

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def ASSIGN(self):
            return self.getToken(MiniGoParser.ASSIGN, 0)

        def expr(self):
            return self.getTypedRuleContext(MiniGoParser.ExprContext,0)


        def SEMI(self):
            return self.getToken(MiniGoParser.SEMI, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_constdecl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitConstdecl" ):
                return visitor.visitConstdecl(self)
            else:
                return visitor.visitChildren(self)




    def constdecl(self):

        localctx = MiniGoParser.ConstdeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_constdecl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 139
            self.match(MiniGoParser.KW_CONST)
            self.state = 140
            self.match(MiniGoParser.ID)
            self.state = 141
            self.match(MiniGoParser.ASSIGN)
            self.state = 142
            self.expr(0)

            self.state = 143
            self.match(MiniGoParser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FuncdeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def KW_FUNC(self):
            return self.getToken(MiniGoParser.KW_FUNC, 0)

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def LPAREN(self):
            return self.getToken(MiniGoParser.LPAREN, 0)

        def RPAREN(self):
            return self.getToken(MiniGoParser.RPAREN, 0)

        def SEMI(self):
            return self.getToken(MiniGoParser.SEMI, 0)

        def paramlist(self):
            return self.getTypedRuleContext(MiniGoParser.ParamlistContext,0)


        def returntype(self):
            return self.getTypedRuleContext(MiniGoParser.ReturntypeContext,0)


        def block(self):
            return self.getTypedRuleContext(MiniGoParser.BlockContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_funcdecl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFuncdecl" ):
                return visitor.visitFuncdecl(self)
            else:
                return visitor.visitChildren(self)




    def funcdecl(self):

        localctx = MiniGoParser.FuncdeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_funcdecl)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 145
            self.match(MiniGoParser.KW_FUNC)
            self.state = 146
            self.match(MiniGoParser.ID)
            self.state = 147
            self.match(MiniGoParser.LPAREN)
            self.state = 149
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==MiniGoParser.ID:
                self.state = 148
                self.paramlist()


            self.state = 151
            self.match(MiniGoParser.RPAREN)
            self.state = 153
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.LBRACK) | (1 << MiniGoParser.KW_STRUCT) | (1 << MiniGoParser.KW_INTERFACE) | (1 << MiniGoParser.KW_STRING) | (1 << MiniGoParser.KW_INT) | (1 << MiniGoParser.KW_FLOAT) | (1 << MiniGoParser.KW_BOOLEAN) | (1 << MiniGoParser.ID))) != 0):
                self.state = 152
                self.returntype()


            self.state = 156
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==MiniGoParser.LBRACE:
                self.state = 155
                self.block()


            self.state = 158
            self.match(MiniGoParser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParamlistContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def param(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniGoParser.ParamContext)
            else:
                return self.getTypedRuleContext(MiniGoParser.ParamContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(MiniGoParser.COMMA)
            else:
                return self.getToken(MiniGoParser.COMMA, i)

        def getRuleIndex(self):
            return MiniGoParser.RULE_paramlist

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParamlist" ):
                return visitor.visitParamlist(self)
            else:
                return visitor.visitChildren(self)




    def paramlist(self):

        localctx = MiniGoParser.ParamlistContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_paramlist)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 160
            self.param()
            self.state = 165
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==MiniGoParser.COMMA:
                self.state = 161
                self.match(MiniGoParser.COMMA)
                self.state = 162
                self.param()
                self.state = 167
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParamContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def identifierList(self):
            return self.getTypedRuleContext(MiniGoParser.IdentifierListContext,0)


        def datatype(self):
            return self.getTypedRuleContext(MiniGoParser.DatatypeContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_param

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParam" ):
                return visitor.visitParam(self)
            else:
                return visitor.visitChildren(self)




    def param(self):

        localctx = MiniGoParser.ParamContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_param)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 168
            self.identifierList()
            self.state = 169
            self.datatype()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IdentifierListContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(MiniGoParser.ID)
            else:
                return self.getToken(MiniGoParser.ID, i)

        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(MiniGoParser.COMMA)
            else:
                return self.getToken(MiniGoParser.COMMA, i)

        def getRuleIndex(self):
            return MiniGoParser.RULE_identifierList

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIdentifierList" ):
                return visitor.visitIdentifierList(self)
            else:
                return visitor.visitChildren(self)




    def identifierList(self):

        localctx = MiniGoParser.IdentifierListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_identifierList)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 171
            self.match(MiniGoParser.ID)
            self.state = 176
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==MiniGoParser.COMMA:
                self.state = 172
                self.match(MiniGoParser.COMMA)
                self.state = 173
                self.match(MiniGoParser.ID)
                self.state = 178
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BlockContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LBRACE(self):
            return self.getToken(MiniGoParser.LBRACE, 0)

        def RBRACE(self):
            return self.getToken(MiniGoParser.RBRACE, 0)

        def stmt(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniGoParser.StmtContext)
            else:
                return self.getTypedRuleContext(MiniGoParser.StmtContext,i)


        def getRuleIndex(self):
            return MiniGoParser.RULE_block

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBlock" ):
                return visitor.visitBlock(self)
            else:
                return visitor.visitChildren(self)




    def block(self):

        localctx = MiniGoParser.BlockContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_block)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 179
            self.match(MiniGoParser.LBRACE)
            self.state = 181 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 180
                self.stmt()
                self.state = 183 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.MINUS) | (1 << MiniGoParser.NOT) | (1 << MiniGoParser.LPAREN) | (1 << MiniGoParser.LBRACK) | (1 << MiniGoParser.KW_IF) | (1 << MiniGoParser.KW_FOR) | (1 << MiniGoParser.KW_RETURN) | (1 << MiniGoParser.KW_CONST) | (1 << MiniGoParser.KW_VAR) | (1 << MiniGoParser.KW_CONTINUE) | (1 << MiniGoParser.KW_BREAK) | (1 << MiniGoParser.KW_NIL) | (1 << MiniGoParser.KW_TRUE) | (1 << MiniGoParser.KW_FALSE) | (1 << MiniGoParser.ID) | (1 << MiniGoParser.INT_LIT) | (1 << MiniGoParser.FLOAT_LIT) | (1 << MiniGoParser.STRING_LIT))) != 0)):
                    break

            self.state = 185
            self.match(MiniGoParser.RBRACE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def callstmt(self):
            return self.getTypedRuleContext(MiniGoParser.CallstmtContext,0)


        def constdecl(self):
            return self.getTypedRuleContext(MiniGoParser.ConstdeclContext,0)


        def vardecl(self):
            return self.getTypedRuleContext(MiniGoParser.VardeclContext,0)


        def ifstmt(self):
            return self.getTypedRuleContext(MiniGoParser.IfstmtContext,0)


        def forstmt(self):
            return self.getTypedRuleContext(MiniGoParser.ForstmtContext,0)


        def returnstmt(self):
            return self.getTypedRuleContext(MiniGoParser.ReturnstmtContext,0)


        def assignstmt(self):
            return self.getTypedRuleContext(MiniGoParser.AssignstmtContext,0)


        def breakstmt(self):
            return self.getTypedRuleContext(MiniGoParser.BreakstmtContext,0)


        def continuestmt(self):
            return self.getTypedRuleContext(MiniGoParser.ContinuestmtContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStmt" ):
                return visitor.visitStmt(self)
            else:
                return visitor.visitChildren(self)




    def stmt(self):

        localctx = MiniGoParser.StmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_stmt)
        try:
            self.state = 196
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,10,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 187
                self.callstmt()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 188
                self.constdecl()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 189
                self.vardecl()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 190
                self.ifstmt()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 191
                self.forstmt()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 192
                self.returnstmt()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 193
                self.assignstmt()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 194
                self.breakstmt()
                pass

            elif la_ == 9:
                self.enterOuterAlt(localctx, 9)
                self.state = 195
                self.continuestmt()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MethoddeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def KW_FUNC(self):
            return self.getToken(MiniGoParser.KW_FUNC, 0)

        def receiver(self):
            return self.getTypedRuleContext(MiniGoParser.ReceiverContext,0)


        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def LPAREN(self):
            return self.getToken(MiniGoParser.LPAREN, 0)

        def RPAREN(self):
            return self.getToken(MiniGoParser.RPAREN, 0)

        def block(self):
            return self.getTypedRuleContext(MiniGoParser.BlockContext,0)


        def SEMI(self):
            return self.getToken(MiniGoParser.SEMI, 0)

        def paramlist(self):
            return self.getTypedRuleContext(MiniGoParser.ParamlistContext,0)


        def returntype(self):
            return self.getTypedRuleContext(MiniGoParser.ReturntypeContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_methoddecl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMethoddecl" ):
                return visitor.visitMethoddecl(self)
            else:
                return visitor.visitChildren(self)




    def methoddecl(self):

        localctx = MiniGoParser.MethoddeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_methoddecl)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 198
            self.match(MiniGoParser.KW_FUNC)
            self.state = 199
            self.receiver()
            self.state = 200
            self.match(MiniGoParser.ID)
            self.state = 201
            self.match(MiniGoParser.LPAREN)
            self.state = 203
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==MiniGoParser.ID:
                self.state = 202
                self.paramlist()


            self.state = 205
            self.match(MiniGoParser.RPAREN)
            self.state = 207
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.LBRACK) | (1 << MiniGoParser.KW_STRUCT) | (1 << MiniGoParser.KW_INTERFACE) | (1 << MiniGoParser.KW_STRING) | (1 << MiniGoParser.KW_INT) | (1 << MiniGoParser.KW_FLOAT) | (1 << MiniGoParser.KW_BOOLEAN) | (1 << MiniGoParser.ID))) != 0):
                self.state = 206
                self.returntype()


            self.state = 209
            self.block()
            self.state = 210
            self.match(MiniGoParser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ReceiverContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LPAREN(self):
            return self.getToken(MiniGoParser.LPAREN, 0)

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(MiniGoParser.ID)
            else:
                return self.getToken(MiniGoParser.ID, i)

        def RPAREN(self):
            return self.getToken(MiniGoParser.RPAREN, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_receiver

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitReceiver" ):
                return visitor.visitReceiver(self)
            else:
                return visitor.visitChildren(self)




    def receiver(self):

        localctx = MiniGoParser.ReceiverContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_receiver)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 212
            self.match(MiniGoParser.LPAREN)
            self.state = 213
            self.match(MiniGoParser.ID)
            self.state = 214
            self.match(MiniGoParser.ID)
            self.state = 215
            self.match(MiniGoParser.RPAREN)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TypedefContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def structType(self):
            return self.getTypedRuleContext(MiniGoParser.StructTypeContext,0)


        def interfaceType(self):
            return self.getTypedRuleContext(MiniGoParser.InterfaceTypeContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_typedef

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTypedef" ):
                return visitor.visitTypedef(self)
            else:
                return visitor.visitChildren(self)




    def typedef(self):

        localctx = MiniGoParser.TypedefContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_typedef)
        try:
            self.state = 219
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,13,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 217
                self.structType()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 218
                self.interfaceType()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StructTypeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def KW_TYPE(self):
            return self.getToken(MiniGoParser.KW_TYPE, 0)

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def KW_STRUCT(self):
            return self.getToken(MiniGoParser.KW_STRUCT, 0)

        def LBRACE(self):
            return self.getToken(MiniGoParser.LBRACE, 0)

        def structfields(self):
            return self.getTypedRuleContext(MiniGoParser.StructfieldsContext,0)


        def RBRACE(self):
            return self.getToken(MiniGoParser.RBRACE, 0)

        def SEMI(self):
            return self.getToken(MiniGoParser.SEMI, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_structType

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStructType" ):
                return visitor.visitStructType(self)
            else:
                return visitor.visitChildren(self)




    def structType(self):

        localctx = MiniGoParser.StructTypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_structType)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 221
            self.match(MiniGoParser.KW_TYPE)
            self.state = 222
            self.match(MiniGoParser.ID)
            self.state = 223
            self.match(MiniGoParser.KW_STRUCT)
            self.state = 224
            self.match(MiniGoParser.LBRACE)
            self.state = 225
            self.structfields()
            self.state = 226
            self.match(MiniGoParser.RBRACE)
            self.state = 227
            self.match(MiniGoParser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StructfieldsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def fielddecl(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniGoParser.FielddeclContext)
            else:
                return self.getTypedRuleContext(MiniGoParser.FielddeclContext,i)


        def getRuleIndex(self):
            return MiniGoParser.RULE_structfields

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStructfields" ):
                return visitor.visitStructfields(self)
            else:
                return visitor.visitChildren(self)




    def structfields(self):

        localctx = MiniGoParser.StructfieldsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_structfields)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 230 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 229
                self.fielddecl()
                self.state = 232 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==MiniGoParser.ID):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FielddeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def datatype(self):
            return self.getTypedRuleContext(MiniGoParser.DatatypeContext,0)


        def SEMI(self):
            return self.getToken(MiniGoParser.SEMI, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_fielddecl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFielddecl" ):
                return visitor.visitFielddecl(self)
            else:
                return visitor.visitChildren(self)




    def fielddecl(self):

        localctx = MiniGoParser.FielddeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_fielddecl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 234
            self.match(MiniGoParser.ID)
            self.state = 235
            self.datatype()
            self.state = 236
            self.match(MiniGoParser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class InterfaceTypeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def KW_TYPE(self):
            return self.getToken(MiniGoParser.KW_TYPE, 0)

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def KW_INTERFACE(self):
            return self.getToken(MiniGoParser.KW_INTERFACE, 0)

        def LBRACE(self):
            return self.getToken(MiniGoParser.LBRACE, 0)

        def interfaceMethodList(self):
            return self.getTypedRuleContext(MiniGoParser.InterfaceMethodListContext,0)


        def RBRACE(self):
            return self.getToken(MiniGoParser.RBRACE, 0)

        def SEMI(self):
            return self.getToken(MiniGoParser.SEMI, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_interfaceType

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInterfaceType" ):
                return visitor.visitInterfaceType(self)
            else:
                return visitor.visitChildren(self)




    def interfaceType(self):

        localctx = MiniGoParser.InterfaceTypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_interfaceType)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 238
            self.match(MiniGoParser.KW_TYPE)
            self.state = 239
            self.match(MiniGoParser.ID)
            self.state = 240
            self.match(MiniGoParser.KW_INTERFACE)
            self.state = 241
            self.match(MiniGoParser.LBRACE)
            self.state = 242
            self.interfaceMethodList()
            self.state = 243
            self.match(MiniGoParser.RBRACE)
            self.state = 244
            self.match(MiniGoParser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class InterfaceMethodListContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def interfaceMethodDecl(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniGoParser.InterfaceMethodDeclContext)
            else:
                return self.getTypedRuleContext(MiniGoParser.InterfaceMethodDeclContext,i)


        def getRuleIndex(self):
            return MiniGoParser.RULE_interfaceMethodList

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInterfaceMethodList" ):
                return visitor.visitInterfaceMethodList(self)
            else:
                return visitor.visitChildren(self)




    def interfaceMethodList(self):

        localctx = MiniGoParser.InterfaceMethodListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_interfaceMethodList)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 247 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 246
                self.interfaceMethodDecl()
                self.state = 249 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==MiniGoParser.ID):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class InterfaceMethodDeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def LPAREN(self):
            return self.getToken(MiniGoParser.LPAREN, 0)

        def RPAREN(self):
            return self.getToken(MiniGoParser.RPAREN, 0)

        def SEMI(self):
            return self.getToken(MiniGoParser.SEMI, 0)

        def paramlist(self):
            return self.getTypedRuleContext(MiniGoParser.ParamlistContext,0)


        def returntype(self):
            return self.getTypedRuleContext(MiniGoParser.ReturntypeContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_interfaceMethodDecl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInterfaceMethodDecl" ):
                return visitor.visitInterfaceMethodDecl(self)
            else:
                return visitor.visitChildren(self)




    def interfaceMethodDecl(self):

        localctx = MiniGoParser.InterfaceMethodDeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_interfaceMethodDecl)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 251
            self.match(MiniGoParser.ID)
            self.state = 252
            self.match(MiniGoParser.LPAREN)
            self.state = 254
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==MiniGoParser.ID:
                self.state = 253
                self.paramlist()


            self.state = 256
            self.match(MiniGoParser.RPAREN)
            self.state = 258
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.LBRACK) | (1 << MiniGoParser.KW_STRUCT) | (1 << MiniGoParser.KW_INTERFACE) | (1 << MiniGoParser.KW_STRING) | (1 << MiniGoParser.KW_INT) | (1 << MiniGoParser.KW_FLOAT) | (1 << MiniGoParser.KW_BOOLEAN) | (1 << MiniGoParser.ID))) != 0):
                self.state = 257
                self.returntype()


            self.state = 260
            self.match(MiniGoParser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CompareContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EQ(self):
            return self.getToken(MiniGoParser.EQ, 0)

        def NEQ(self):
            return self.getToken(MiniGoParser.NEQ, 0)

        def LT(self):
            return self.getToken(MiniGoParser.LT, 0)

        def LE(self):
            return self.getToken(MiniGoParser.LE, 0)

        def GT(self):
            return self.getToken(MiniGoParser.GT, 0)

        def GE(self):
            return self.getToken(MiniGoParser.GE, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_compare

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCompare" ):
                return visitor.visitCompare(self)
            else:
                return visitor.visitChildren(self)




    def compare(self):

        localctx = MiniGoParser.CompareContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_compare)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 262
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.EQ) | (1 << MiniGoParser.NEQ) | (1 << MiniGoParser.LT) | (1 << MiniGoParser.LE) | (1 << MiniGoParser.GT) | (1 << MiniGoParser.GE))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return MiniGoParser.RULE_expr

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)


    class BooleanOrOpContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MiniGoParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self):
            return self.getTypedRuleContext(MiniGoParser.ExprContext,0)

        def OR(self):
            return self.getToken(MiniGoParser.OR, 0)
        def expr1(self):
            return self.getTypedRuleContext(MiniGoParser.Expr1Context,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBooleanOrOp" ):
                return visitor.visitBooleanOrOp(self)
            else:
                return visitor.visitChildren(self)


    class Ex1Context(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MiniGoParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr1(self):
            return self.getTypedRuleContext(MiniGoParser.Expr1Context,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitEx1" ):
                return visitor.visitEx1(self)
            else:
                return visitor.visitChildren(self)



    def expr(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = MiniGoParser.ExprContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 42
        self.enterRecursionRule(localctx, 42, self.RULE_expr, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            localctx = MiniGoParser.Ex1Context(self, localctx)
            self._ctx = localctx
            _prevctx = localctx

            self.state = 265
            self.expr1(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 272
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,18,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MiniGoParser.BooleanOrOpContext(self, MiniGoParser.ExprContext(self, _parentctx, _parentState))
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                    self.state = 267
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 268
                    self.match(MiniGoParser.OR)
                    self.state = 269
                    self.expr1(0) 
                self.state = 274
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,18,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Expr1Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return MiniGoParser.RULE_expr1

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)


    class BooleanAndOpContext(Expr1Context):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MiniGoParser.Expr1Context
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr1(self):
            return self.getTypedRuleContext(MiniGoParser.Expr1Context,0)

        def AND(self):
            return self.getToken(MiniGoParser.AND, 0)
        def expr2(self):
            return self.getTypedRuleContext(MiniGoParser.Expr2Context,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBooleanAndOp" ):
                return visitor.visitBooleanAndOp(self)
            else:
                return visitor.visitChildren(self)


    class Ex2Context(Expr1Context):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MiniGoParser.Expr1Context
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr2(self):
            return self.getTypedRuleContext(MiniGoParser.Expr2Context,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitEx2" ):
                return visitor.visitEx2(self)
            else:
                return visitor.visitChildren(self)



    def expr1(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = MiniGoParser.Expr1Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 44
        self.enterRecursionRule(localctx, 44, self.RULE_expr1, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            localctx = MiniGoParser.Ex2Context(self, localctx)
            self._ctx = localctx
            _prevctx = localctx

            self.state = 276
            self.expr2(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 283
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,19,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MiniGoParser.BooleanAndOpContext(self, MiniGoParser.Expr1Context(self, _parentctx, _parentState))
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr1)
                    self.state = 278
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 279
                    self.match(MiniGoParser.AND)
                    self.state = 280
                    self.expr2(0) 
                self.state = 285
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,19,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Expr2Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return MiniGoParser.RULE_expr2

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)


    class Ex3Context(Expr2Context):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MiniGoParser.Expr2Context
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr3(self):
            return self.getTypedRuleContext(MiniGoParser.Expr3Context,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitEx3" ):
                return visitor.visitEx3(self)
            else:
                return visitor.visitChildren(self)


    class RelationalOpContext(Expr2Context):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MiniGoParser.Expr2Context
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr2(self):
            return self.getTypedRuleContext(MiniGoParser.Expr2Context,0)

        def compare(self):
            return self.getTypedRuleContext(MiniGoParser.CompareContext,0)

        def expr3(self):
            return self.getTypedRuleContext(MiniGoParser.Expr3Context,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRelationalOp" ):
                return visitor.visitRelationalOp(self)
            else:
                return visitor.visitChildren(self)



    def expr2(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = MiniGoParser.Expr2Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 46
        self.enterRecursionRule(localctx, 46, self.RULE_expr2, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            localctx = MiniGoParser.Ex3Context(self, localctx)
            self._ctx = localctx
            _prevctx = localctx

            self.state = 287
            self.expr3(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 295
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,20,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MiniGoParser.RelationalOpContext(self, MiniGoParser.Expr2Context(self, _parentctx, _parentState))
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr2)
                    self.state = 289
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 290
                    self.compare()
                    self.state = 291
                    self.expr3(0) 
                self.state = 297
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,20,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Expr3Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return MiniGoParser.RULE_expr3

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)


    class Ex4Context(Expr3Context):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MiniGoParser.Expr3Context
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr4(self):
            return self.getTypedRuleContext(MiniGoParser.Expr4Context,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitEx4" ):
                return visitor.visitEx4(self)
            else:
                return visitor.visitChildren(self)


    class MathOp1Context(Expr3Context):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MiniGoParser.Expr3Context
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr3(self):
            return self.getTypedRuleContext(MiniGoParser.Expr3Context,0)

        def expr4(self):
            return self.getTypedRuleContext(MiniGoParser.Expr4Context,0)

        def PLUS(self):
            return self.getToken(MiniGoParser.PLUS, 0)
        def MINUS(self):
            return self.getToken(MiniGoParser.MINUS, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMathOp1" ):
                return visitor.visitMathOp1(self)
            else:
                return visitor.visitChildren(self)



    def expr3(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = MiniGoParser.Expr3Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 48
        self.enterRecursionRule(localctx, 48, self.RULE_expr3, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            localctx = MiniGoParser.Ex4Context(self, localctx)
            self._ctx = localctx
            _prevctx = localctx

            self.state = 299
            self.expr4(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 306
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,21,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MiniGoParser.MathOp1Context(self, MiniGoParser.Expr3Context(self, _parentctx, _parentState))
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr3)
                    self.state = 301
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 302
                    _la = self._input.LA(1)
                    if not(_la==MiniGoParser.PLUS or _la==MiniGoParser.MINUS):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 303
                    self.expr4(0) 
                self.state = 308
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,21,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Expr4Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return MiniGoParser.RULE_expr4

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)


    class Ex5Context(Expr4Context):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MiniGoParser.Expr4Context
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr5(self):
            return self.getTypedRuleContext(MiniGoParser.Expr5Context,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitEx5" ):
                return visitor.visitEx5(self)
            else:
                return visitor.visitChildren(self)


    class MathOp2Context(Expr4Context):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MiniGoParser.Expr4Context
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr4(self):
            return self.getTypedRuleContext(MiniGoParser.Expr4Context,0)

        def expr5(self):
            return self.getTypedRuleContext(MiniGoParser.Expr5Context,0)

        def MULT(self):
            return self.getToken(MiniGoParser.MULT, 0)
        def DIV(self):
            return self.getToken(MiniGoParser.DIV, 0)
        def MOD(self):
            return self.getToken(MiniGoParser.MOD, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMathOp2" ):
                return visitor.visitMathOp2(self)
            else:
                return visitor.visitChildren(self)



    def expr4(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = MiniGoParser.Expr4Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 50
        self.enterRecursionRule(localctx, 50, self.RULE_expr4, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            localctx = MiniGoParser.Ex5Context(self, localctx)
            self._ctx = localctx
            _prevctx = localctx

            self.state = 310
            self.expr5()
            self._ctx.stop = self._input.LT(-1)
            self.state = 317
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,22,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MiniGoParser.MathOp2Context(self, MiniGoParser.Expr4Context(self, _parentctx, _parentState))
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr4)
                    self.state = 312
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 313
                    _la = self._input.LA(1)
                    if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.MULT) | (1 << MiniGoParser.DIV) | (1 << MiniGoParser.MOD))) != 0)):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 314
                    self.expr5() 
                self.state = 319
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,22,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Expr5Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return MiniGoParser.RULE_expr5

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class Ex6Context(Expr5Context):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MiniGoParser.Expr5Context
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr6(self):
            return self.getTypedRuleContext(MiniGoParser.Expr6Context,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitEx6" ):
                return visitor.visitEx6(self)
            else:
                return visitor.visitChildren(self)


    class UnaryOpContext(Expr5Context):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MiniGoParser.Expr5Context
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr5(self):
            return self.getTypedRuleContext(MiniGoParser.Expr5Context,0)

        def NOT(self):
            return self.getToken(MiniGoParser.NOT, 0)
        def MINUS(self):
            return self.getToken(MiniGoParser.MINUS, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitUnaryOp" ):
                return visitor.visitUnaryOp(self)
            else:
                return visitor.visitChildren(self)



    def expr5(self):

        localctx = MiniGoParser.Expr5Context(self, self._ctx, self.state)
        self.enterRule(localctx, 52, self.RULE_expr5)
        self._la = 0 # Token type
        try:
            self.state = 323
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.MINUS, MiniGoParser.NOT]:
                localctx = MiniGoParser.UnaryOpContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 320
                _la = self._input.LA(1)
                if not(_la==MiniGoParser.MINUS or _la==MiniGoParser.NOT):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 321
                self.expr5()
                pass
            elif token in [MiniGoParser.LPAREN, MiniGoParser.LBRACK, MiniGoParser.KW_NIL, MiniGoParser.KW_TRUE, MiniGoParser.KW_FALSE, MiniGoParser.ID, MiniGoParser.INT_LIT, MiniGoParser.FLOAT_LIT, MiniGoParser.STRING_LIT]:
                localctx = MiniGoParser.Ex6Context(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 322
                self.expr6(0)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Expr6Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return MiniGoParser.RULE_expr6

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)


    class Ex7Context(Expr6Context):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MiniGoParser.Expr6Context
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr7(self):
            return self.getTypedRuleContext(MiniGoParser.Expr7Context,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitEx7" ):
                return visitor.visitEx7(self)
            else:
                return visitor.visitChildren(self)


    class FieldAccessContext(Expr6Context):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MiniGoParser.Expr6Context
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr6(self):
            return self.getTypedRuleContext(MiniGoParser.Expr6Context,0)

        def DOT(self):
            return self.getToken(MiniGoParser.DOT, 0)
        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFieldAccess" ):
                return visitor.visitFieldAccess(self)
            else:
                return visitor.visitChildren(self)


    class MethodCallexpContext(Expr6Context):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MiniGoParser.Expr6Context
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr6(self):
            return self.getTypedRuleContext(MiniGoParser.Expr6Context,0)

        def DOT(self):
            return self.getToken(MiniGoParser.DOT, 0)
        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)
        def LPAREN(self):
            return self.getToken(MiniGoParser.LPAREN, 0)
        def RPAREN(self):
            return self.getToken(MiniGoParser.RPAREN, 0)
        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniGoParser.ExprContext)
            else:
                return self.getTypedRuleContext(MiniGoParser.ExprContext,i)

        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(MiniGoParser.COMMA)
            else:
                return self.getToken(MiniGoParser.COMMA, i)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMethodCallexp" ):
                return visitor.visitMethodCallexp(self)
            else:
                return visitor.visitChildren(self)


    class ArrayAccessContext(Expr6Context):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MiniGoParser.Expr6Context
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr6(self):
            return self.getTypedRuleContext(MiniGoParser.Expr6Context,0)

        def LBRACK(self):
            return self.getToken(MiniGoParser.LBRACK, 0)
        def expr(self):
            return self.getTypedRuleContext(MiniGoParser.ExprContext,0)

        def RBRACK(self):
            return self.getToken(MiniGoParser.RBRACK, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArrayAccess" ):
                return visitor.visitArrayAccess(self)
            else:
                return visitor.visitChildren(self)



    def expr6(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = MiniGoParser.Expr6Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 54
        self.enterRecursionRule(localctx, 54, self.RULE_expr6, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            localctx = MiniGoParser.Ex7Context(self, localctx)
            self._ctx = localctx
            _prevctx = localctx

            self.state = 326
            self.expr7()
            self._ctx.stop = self._input.LT(-1)
            self.state = 353
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,27,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 351
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,26,self._ctx)
                    if la_ == 1:
                        localctx = MiniGoParser.ArrayAccessContext(self, MiniGoParser.Expr6Context(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr6)
                        self.state = 328
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 329
                        self.match(MiniGoParser.LBRACK)
                        self.state = 330
                        self.expr(0)
                        self.state = 331
                        self.match(MiniGoParser.RBRACK)
                        pass

                    elif la_ == 2:
                        localctx = MiniGoParser.MethodCallexpContext(self, MiniGoParser.Expr6Context(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr6)
                        self.state = 333
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 334
                        self.match(MiniGoParser.DOT)
                        self.state = 335
                        self.match(MiniGoParser.ID)
                        self.state = 336
                        self.match(MiniGoParser.LPAREN)
                        self.state = 345
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)
                        if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.MINUS) | (1 << MiniGoParser.NOT) | (1 << MiniGoParser.LPAREN) | (1 << MiniGoParser.LBRACK) | (1 << MiniGoParser.KW_NIL) | (1 << MiniGoParser.KW_TRUE) | (1 << MiniGoParser.KW_FALSE) | (1 << MiniGoParser.ID) | (1 << MiniGoParser.INT_LIT) | (1 << MiniGoParser.FLOAT_LIT) | (1 << MiniGoParser.STRING_LIT))) != 0):
                            self.state = 337
                            self.expr(0)
                            self.state = 342
                            self._errHandler.sync(self)
                            _la = self._input.LA(1)
                            while _la==MiniGoParser.COMMA:
                                self.state = 338
                                self.match(MiniGoParser.COMMA)
                                self.state = 339
                                self.expr(0)
                                self.state = 344
                                self._errHandler.sync(self)
                                _la = self._input.LA(1)



                        self.state = 347
                        self.match(MiniGoParser.RPAREN)
                        pass

                    elif la_ == 3:
                        localctx = MiniGoParser.FieldAccessContext(self, MiniGoParser.Expr6Context(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr6)
                        self.state = 348
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 349
                        self.match(MiniGoParser.DOT)
                        self.state = 350
                        self.match(MiniGoParser.ID)
                        pass

             
                self.state = 355
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,27,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Expr7Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return MiniGoParser.RULE_expr7

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class FunctionCallexpContext(Expr7Context):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MiniGoParser.Expr7Context
            super().__init__(parser)
            self.copyFrom(ctx)

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)
        def LPAREN(self):
            return self.getToken(MiniGoParser.LPAREN, 0)
        def RPAREN(self):
            return self.getToken(MiniGoParser.RPAREN, 0)
        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniGoParser.ExprContext)
            else:
                return self.getTypedRuleContext(MiniGoParser.ExprContext,i)

        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(MiniGoParser.COMMA)
            else:
                return self.getToken(MiniGoParser.COMMA, i)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunctionCallexp" ):
                return visitor.visitFunctionCallexp(self)
            else:
                return visitor.visitChildren(self)


    class CobanContext(Expr7Context):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MiniGoParser.Expr7Context
            super().__init__(parser)
            self.copyFrom(ctx)

        def term(self):
            return self.getTypedRuleContext(MiniGoParser.TermContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCoban" ):
                return visitor.visitCoban(self)
            else:
                return visitor.visitChildren(self)


    class ParenExprContext(Expr7Context):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MiniGoParser.Expr7Context
            super().__init__(parser)
            self.copyFrom(ctx)

        def LPAREN(self):
            return self.getToken(MiniGoParser.LPAREN, 0)
        def expr(self):
            return self.getTypedRuleContext(MiniGoParser.ExprContext,0)

        def RPAREN(self):
            return self.getToken(MiniGoParser.RPAREN, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParenExpr" ):
                return visitor.visitParenExpr(self)
            else:
                return visitor.visitChildren(self)



    def expr7(self):

        localctx = MiniGoParser.Expr7Context(self, self._ctx, self.state)
        self.enterRule(localctx, 56, self.RULE_expr7)
        self._la = 0 # Token type
        try:
            self.state = 374
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,30,self._ctx)
            if la_ == 1:
                localctx = MiniGoParser.ParenExprContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 356
                self.match(MiniGoParser.LPAREN)
                self.state = 357
                self.expr(0)
                self.state = 358
                self.match(MiniGoParser.RPAREN)
                pass

            elif la_ == 2:
                localctx = MiniGoParser.FunctionCallexpContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 360
                self.match(MiniGoParser.ID)
                self.state = 361
                self.match(MiniGoParser.LPAREN)
                self.state = 370
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.MINUS) | (1 << MiniGoParser.NOT) | (1 << MiniGoParser.LPAREN) | (1 << MiniGoParser.LBRACK) | (1 << MiniGoParser.KW_NIL) | (1 << MiniGoParser.KW_TRUE) | (1 << MiniGoParser.KW_FALSE) | (1 << MiniGoParser.ID) | (1 << MiniGoParser.INT_LIT) | (1 << MiniGoParser.FLOAT_LIT) | (1 << MiniGoParser.STRING_LIT))) != 0):
                    self.state = 362
                    self.expr(0)
                    self.state = 367
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    while _la==MiniGoParser.COMMA:
                        self.state = 363
                        self.match(MiniGoParser.COMMA)
                        self.state = 364
                        self.expr(0)
                        self.state = 369
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)



                self.state = 372
                self.match(MiniGoParser.RPAREN)
                pass

            elif la_ == 3:
                localctx = MiniGoParser.CobanContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 373
                self.term()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TermContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return MiniGoParser.RULE_term

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class StructLiteraltermContext(TermContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MiniGoParser.TermContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def structliteral(self):
            return self.getTypedRuleContext(MiniGoParser.StructliteralContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStructLiteralterm" ):
                return visitor.visitStructLiteralterm(self)
            else:
                return visitor.visitChildren(self)


    class IdentifierContext(TermContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MiniGoParser.TermContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIdentifier" ):
                return visitor.visitIdentifier(self)
            else:
                return visitor.visitChildren(self)


    class FalseLiteralContext(TermContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MiniGoParser.TermContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def KW_FALSE(self):
            return self.getToken(MiniGoParser.KW_FALSE, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFalseLiteral" ):
                return visitor.visitFalseLiteral(self)
            else:
                return visitor.visitChildren(self)


    class StringLiteralContext(TermContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MiniGoParser.TermContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def STRING_LIT(self):
            return self.getToken(MiniGoParser.STRING_LIT, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStringLiteral" ):
                return visitor.visitStringLiteral(self)
            else:
                return visitor.visitChildren(self)


    class IntLiteralContext(TermContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MiniGoParser.TermContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def INT_LIT(self):
            return self.getToken(MiniGoParser.INT_LIT, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIntLiteral" ):
                return visitor.visitIntLiteral(self)
            else:
                return visitor.visitChildren(self)


    class FloatLiteralContext(TermContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MiniGoParser.TermContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def FLOAT_LIT(self):
            return self.getToken(MiniGoParser.FLOAT_LIT, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFloatLiteral" ):
                return visitor.visitFloatLiteral(self)
            else:
                return visitor.visitChildren(self)


    class NilLiteralContext(TermContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MiniGoParser.TermContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def KW_NIL(self):
            return self.getToken(MiniGoParser.KW_NIL, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNilLiteral" ):
                return visitor.visitNilLiteral(self)
            else:
                return visitor.visitChildren(self)


    class TrueLiteralContext(TermContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MiniGoParser.TermContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def KW_TRUE(self):
            return self.getToken(MiniGoParser.KW_TRUE, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTrueLiteral" ):
                return visitor.visitTrueLiteral(self)
            else:
                return visitor.visitChildren(self)


    class ArrayLiteraltermContext(TermContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MiniGoParser.TermContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def arrayliteral(self):
            return self.getTypedRuleContext(MiniGoParser.ArrayliteralContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArrayLiteralterm" ):
                return visitor.visitArrayLiteralterm(self)
            else:
                return visitor.visitChildren(self)



    def term(self):

        localctx = MiniGoParser.TermContext(self, self._ctx, self.state)
        self.enterRule(localctx, 58, self.RULE_term)
        try:
            self.state = 385
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,31,self._ctx)
            if la_ == 1:
                localctx = MiniGoParser.IdentifierContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 376
                self.match(MiniGoParser.ID)
                pass

            elif la_ == 2:
                localctx = MiniGoParser.IntLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 377
                self.match(MiniGoParser.INT_LIT)
                pass

            elif la_ == 3:
                localctx = MiniGoParser.FloatLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 378
                self.match(MiniGoParser.FLOAT_LIT)
                pass

            elif la_ == 4:
                localctx = MiniGoParser.StringLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 379
                self.match(MiniGoParser.STRING_LIT)
                pass

            elif la_ == 5:
                localctx = MiniGoParser.ArrayLiteraltermContext(self, localctx)
                self.enterOuterAlt(localctx, 5)
                self.state = 380
                self.arrayliteral()
                pass

            elif la_ == 6:
                localctx = MiniGoParser.StructLiteraltermContext(self, localctx)
                self.enterOuterAlt(localctx, 6)
                self.state = 381
                self.structliteral()
                pass

            elif la_ == 7:
                localctx = MiniGoParser.TrueLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 7)
                self.state = 382
                self.match(MiniGoParser.KW_TRUE)
                pass

            elif la_ == 8:
                localctx = MiniGoParser.FalseLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 8)
                self.state = 383
                self.match(MiniGoParser.KW_FALSE)
                pass

            elif la_ == 9:
                localctx = MiniGoParser.NilLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 9)
                self.state = 384
                self.match(MiniGoParser.KW_NIL)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StructliteralContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def structliteralbody(self):
            return self.getTypedRuleContext(MiniGoParser.StructliteralbodyContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_structliteral

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStructliteral" ):
                return visitor.visitStructliteral(self)
            else:
                return visitor.visitChildren(self)




    def structliteral(self):

        localctx = MiniGoParser.StructliteralContext(self, self._ctx, self.state)
        self.enterRule(localctx, 60, self.RULE_structliteral)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 387
            self.match(MiniGoParser.ID)
            self.state = 388
            self.structliteralbody()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StructliteralbodyContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LBRACE(self):
            return self.getToken(MiniGoParser.LBRACE, 0)

        def RBRACE(self):
            return self.getToken(MiniGoParser.RBRACE, 0)

        def fieldinit(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniGoParser.FieldinitContext)
            else:
                return self.getTypedRuleContext(MiniGoParser.FieldinitContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(MiniGoParser.COMMA)
            else:
                return self.getToken(MiniGoParser.COMMA, i)

        def getRuleIndex(self):
            return MiniGoParser.RULE_structliteralbody

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStructliteralbody" ):
                return visitor.visitStructliteralbody(self)
            else:
                return visitor.visitChildren(self)




    def structliteralbody(self):

        localctx = MiniGoParser.StructliteralbodyContext(self, self._ctx, self.state)
        self.enterRule(localctx, 62, self.RULE_structliteralbody)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 390
            self.match(MiniGoParser.LBRACE)
            self.state = 399
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==MiniGoParser.ID:
                self.state = 391
                self.fieldinit()
                self.state = 396
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==MiniGoParser.COMMA:
                    self.state = 392
                    self.match(MiniGoParser.COMMA)
                    self.state = 393
                    self.fieldinit()
                    self.state = 398
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)



            self.state = 401
            self.match(MiniGoParser.RBRACE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FieldinitContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def COLON(self):
            return self.getToken(MiniGoParser.COLON, 0)

        def expr(self):
            return self.getTypedRuleContext(MiniGoParser.ExprContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_fieldinit

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFieldinit" ):
                return visitor.visitFieldinit(self)
            else:
                return visitor.visitChildren(self)




    def fieldinit(self):

        localctx = MiniGoParser.FieldinitContext(self, self._ctx, self.state)
        self.enterRule(localctx, 64, self.RULE_fieldinit)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 403
            self.match(MiniGoParser.ID)
            self.state = 404
            self.match(MiniGoParser.COLON)
            self.state = 405
            self.expr(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LvalueContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def lvalue(self):
            return self.getTypedRuleContext(MiniGoParser.LvalueContext,0)


        def LBRACK(self):
            return self.getToken(MiniGoParser.LBRACK, 0)

        def expr(self):
            return self.getTypedRuleContext(MiniGoParser.ExprContext,0)


        def RBRACK(self):
            return self.getToken(MiniGoParser.RBRACK, 0)

        def DOT(self):
            return self.getToken(MiniGoParser.DOT, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_lvalue

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLvalue" ):
                return visitor.visitLvalue(self)
            else:
                return visitor.visitChildren(self)



    def lvalue(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = MiniGoParser.LvalueContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 66
        self.enterRecursionRule(localctx, 66, self.RULE_lvalue, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 408
            self.match(MiniGoParser.ID)
            self._ctx.stop = self._input.LT(-1)
            self.state = 420
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,35,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 418
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,34,self._ctx)
                    if la_ == 1:
                        localctx = MiniGoParser.LvalueContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_lvalue)
                        self.state = 410
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 411
                        self.match(MiniGoParser.LBRACK)
                        self.state = 412
                        self.expr(0)
                        self.state = 413
                        self.match(MiniGoParser.RBRACK)
                        pass

                    elif la_ == 2:
                        localctx = MiniGoParser.LvalueContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_lvalue)
                        self.state = 415
                        if not self.precpred(self._ctx, 1):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                        self.state = 416
                        self.match(MiniGoParser.DOT)
                        self.state = 417
                        self.match(MiniGoParser.ID)
                        pass

             
                self.state = 422
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,35,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Assign_opContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ASSIGN_INIT(self):
            return self.getToken(MiniGoParser.ASSIGN_INIT, 0)

        def ADD_ASSIGN(self):
            return self.getToken(MiniGoParser.ADD_ASSIGN, 0)

        def SUB_ASSIGN(self):
            return self.getToken(MiniGoParser.SUB_ASSIGN, 0)

        def MUL_ASSIGN(self):
            return self.getToken(MiniGoParser.MUL_ASSIGN, 0)

        def DIV_ASSIGN(self):
            return self.getToken(MiniGoParser.DIV_ASSIGN, 0)

        def MOD_ASSIGN(self):
            return self.getToken(MiniGoParser.MOD_ASSIGN, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_assign_op

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssign_op" ):
                return visitor.visitAssign_op(self)
            else:
                return visitor.visitChildren(self)




    def assign_op(self):

        localctx = MiniGoParser.Assign_opContext(self, self._ctx, self.state)
        self.enterRule(localctx, 68, self.RULE_assign_op)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 423
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.ASSIGN_INIT) | (1 << MiniGoParser.ADD_ASSIGN) | (1 << MiniGoParser.SUB_ASSIGN) | (1 << MiniGoParser.MUL_ASSIGN) | (1 << MiniGoParser.DIV_ASSIGN) | (1 << MiniGoParser.MOD_ASSIGN))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AssignstmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def lvalue(self):
            return self.getTypedRuleContext(MiniGoParser.LvalueContext,0)


        def assign_op(self):
            return self.getTypedRuleContext(MiniGoParser.Assign_opContext,0)


        def expr(self):
            return self.getTypedRuleContext(MiniGoParser.ExprContext,0)


        def SEMI(self):
            return self.getToken(MiniGoParser.SEMI, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_assignstmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssignstmt" ):
                return visitor.visitAssignstmt(self)
            else:
                return visitor.visitChildren(self)




    def assignstmt(self):

        localctx = MiniGoParser.AssignstmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 70, self.RULE_assignstmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 425
            self.lvalue(0)
            self.state = 426
            self.assign_op()
            self.state = 427
            self.expr(0)
            self.state = 428
            self.match(MiniGoParser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ReturnstmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def KW_RETURN(self):
            return self.getToken(MiniGoParser.KW_RETURN, 0)

        def SEMI(self):
            return self.getToken(MiniGoParser.SEMI, 0)

        def expr(self):
            return self.getTypedRuleContext(MiniGoParser.ExprContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_returnstmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitReturnstmt" ):
                return visitor.visitReturnstmt(self)
            else:
                return visitor.visitChildren(self)




    def returnstmt(self):

        localctx = MiniGoParser.ReturnstmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 72, self.RULE_returnstmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 430
            self.match(MiniGoParser.KW_RETURN)
            self.state = 432
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.MINUS) | (1 << MiniGoParser.NOT) | (1 << MiniGoParser.LPAREN) | (1 << MiniGoParser.LBRACK) | (1 << MiniGoParser.KW_NIL) | (1 << MiniGoParser.KW_TRUE) | (1 << MiniGoParser.KW_FALSE) | (1 << MiniGoParser.ID) | (1 << MiniGoParser.INT_LIT) | (1 << MiniGoParser.FLOAT_LIT) | (1 << MiniGoParser.STRING_LIT))) != 0):
                self.state = 431
                self.expr(0)


            self.state = 434
            self.match(MiniGoParser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CallstmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return MiniGoParser.RULE_callstmt

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class FunctioncallContext(CallstmtContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MiniGoParser.CallstmtContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)
        def LPAREN(self):
            return self.getToken(MiniGoParser.LPAREN, 0)
        def RPAREN(self):
            return self.getToken(MiniGoParser.RPAREN, 0)
        def SEMI(self):
            return self.getToken(MiniGoParser.SEMI, 0)
        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniGoParser.ExprContext)
            else:
                return self.getTypedRuleContext(MiniGoParser.ExprContext,i)

        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(MiniGoParser.COMMA)
            else:
                return self.getToken(MiniGoParser.COMMA, i)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunctioncall" ):
                return visitor.visitFunctioncall(self)
            else:
                return visitor.visitChildren(self)


    class MethodcallContext(CallstmtContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MiniGoParser.CallstmtContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniGoParser.ExprContext)
            else:
                return self.getTypedRuleContext(MiniGoParser.ExprContext,i)

        def DOT(self):
            return self.getToken(MiniGoParser.DOT, 0)
        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)
        def LPAREN(self):
            return self.getToken(MiniGoParser.LPAREN, 0)
        def RPAREN(self):
            return self.getToken(MiniGoParser.RPAREN, 0)
        def SEMI(self):
            return self.getToken(MiniGoParser.SEMI, 0)
        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(MiniGoParser.COMMA)
            else:
                return self.getToken(MiniGoParser.COMMA, i)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMethodcall" ):
                return visitor.visitMethodcall(self)
            else:
                return visitor.visitChildren(self)



    def callstmt(self):

        localctx = MiniGoParser.CallstmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 74, self.RULE_callstmt)
        self._la = 0 # Token type
        try:
            self.state = 467
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,41,self._ctx)
            if la_ == 1:
                localctx = MiniGoParser.FunctioncallContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 436
                self.match(MiniGoParser.ID)
                self.state = 437
                self.match(MiniGoParser.LPAREN)
                self.state = 446
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.MINUS) | (1 << MiniGoParser.NOT) | (1 << MiniGoParser.LPAREN) | (1 << MiniGoParser.LBRACK) | (1 << MiniGoParser.KW_NIL) | (1 << MiniGoParser.KW_TRUE) | (1 << MiniGoParser.KW_FALSE) | (1 << MiniGoParser.ID) | (1 << MiniGoParser.INT_LIT) | (1 << MiniGoParser.FLOAT_LIT) | (1 << MiniGoParser.STRING_LIT))) != 0):
                    self.state = 438
                    self.expr(0)
                    self.state = 443
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    while _la==MiniGoParser.COMMA:
                        self.state = 439
                        self.match(MiniGoParser.COMMA)
                        self.state = 440
                        self.expr(0)
                        self.state = 445
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)



                self.state = 448
                self.match(MiniGoParser.RPAREN)
                self.state = 449
                self.match(MiniGoParser.SEMI)
                pass

            elif la_ == 2:
                localctx = MiniGoParser.MethodcallContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 450
                self.expr(0)
                self.state = 451
                self.match(MiniGoParser.DOT)
                self.state = 452
                self.match(MiniGoParser.ID)
                self.state = 453
                self.match(MiniGoParser.LPAREN)
                self.state = 462
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.MINUS) | (1 << MiniGoParser.NOT) | (1 << MiniGoParser.LPAREN) | (1 << MiniGoParser.LBRACK) | (1 << MiniGoParser.KW_NIL) | (1 << MiniGoParser.KW_TRUE) | (1 << MiniGoParser.KW_FALSE) | (1 << MiniGoParser.ID) | (1 << MiniGoParser.INT_LIT) | (1 << MiniGoParser.FLOAT_LIT) | (1 << MiniGoParser.STRING_LIT))) != 0):
                    self.state = 454
                    self.expr(0)
                    self.state = 459
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    while _la==MiniGoParser.COMMA:
                        self.state = 455
                        self.match(MiniGoParser.COMMA)
                        self.state = 456
                        self.expr(0)
                        self.state = 461
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)



                self.state = 464
                self.match(MiniGoParser.RPAREN)
                self.state = 465
                self.match(MiniGoParser.SEMI)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BreakstmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def KW_BREAK(self):
            return self.getToken(MiniGoParser.KW_BREAK, 0)

        def SEMI(self):
            return self.getToken(MiniGoParser.SEMI, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_breakstmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBreakstmt" ):
                return visitor.visitBreakstmt(self)
            else:
                return visitor.visitChildren(self)




    def breakstmt(self):

        localctx = MiniGoParser.BreakstmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 76, self.RULE_breakstmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 469
            self.match(MiniGoParser.KW_BREAK)
            self.state = 470
            self.match(MiniGoParser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ContinuestmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def KW_CONTINUE(self):
            return self.getToken(MiniGoParser.KW_CONTINUE, 0)

        def SEMI(self):
            return self.getToken(MiniGoParser.SEMI, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_continuestmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitContinuestmt" ):
                return visitor.visitContinuestmt(self)
            else:
                return visitor.visitChildren(self)




    def continuestmt(self):

        localctx = MiniGoParser.ContinuestmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 78, self.RULE_continuestmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 472
            self.match(MiniGoParser.KW_CONTINUE)
            self.state = 473
            self.match(MiniGoParser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IfstmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def KW_IF(self):
            return self.getToken(MiniGoParser.KW_IF, 0)

        def LPAREN(self):
            return self.getToken(MiniGoParser.LPAREN, 0)

        def expr(self):
            return self.getTypedRuleContext(MiniGoParser.ExprContext,0)


        def RPAREN(self):
            return self.getToken(MiniGoParser.RPAREN, 0)

        def block(self):
            return self.getTypedRuleContext(MiniGoParser.BlockContext,0)


        def SEMI(self):
            return self.getToken(MiniGoParser.SEMI, 0)

        def elseifstmt(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniGoParser.ElseifstmtContext)
            else:
                return self.getTypedRuleContext(MiniGoParser.ElseifstmtContext,i)


        def elsestmt(self):
            return self.getTypedRuleContext(MiniGoParser.ElsestmtContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_ifstmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIfstmt" ):
                return visitor.visitIfstmt(self)
            else:
                return visitor.visitChildren(self)




    def ifstmt(self):

        localctx = MiniGoParser.IfstmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 80, self.RULE_ifstmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 475
            self.match(MiniGoParser.KW_IF)
            self.state = 476
            self.match(MiniGoParser.LPAREN)
            self.state = 477
            self.expr(0)
            self.state = 478
            self.match(MiniGoParser.RPAREN)
            self.state = 479
            self.block()
            self.state = 483
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,42,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 480
                    self.elseifstmt() 
                self.state = 485
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,42,self._ctx)

            self.state = 487
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==MiniGoParser.KW_ELSE:
                self.state = 486
                self.elsestmt()


            self.state = 489
            self.match(MiniGoParser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ElseifstmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def KW_ELSE(self):
            return self.getToken(MiniGoParser.KW_ELSE, 0)

        def KW_IF(self):
            return self.getToken(MiniGoParser.KW_IF, 0)

        def LPAREN(self):
            return self.getToken(MiniGoParser.LPAREN, 0)

        def expr(self):
            return self.getTypedRuleContext(MiniGoParser.ExprContext,0)


        def RPAREN(self):
            return self.getToken(MiniGoParser.RPAREN, 0)

        def block(self):
            return self.getTypedRuleContext(MiniGoParser.BlockContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_elseifstmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitElseifstmt" ):
                return visitor.visitElseifstmt(self)
            else:
                return visitor.visitChildren(self)




    def elseifstmt(self):

        localctx = MiniGoParser.ElseifstmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 82, self.RULE_elseifstmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 491
            self.match(MiniGoParser.KW_ELSE)
            self.state = 492
            self.match(MiniGoParser.KW_IF)
            self.state = 493
            self.match(MiniGoParser.LPAREN)
            self.state = 494
            self.expr(0)
            self.state = 495
            self.match(MiniGoParser.RPAREN)
            self.state = 496
            self.block()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ElsestmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def KW_ELSE(self):
            return self.getToken(MiniGoParser.KW_ELSE, 0)

        def block(self):
            return self.getTypedRuleContext(MiniGoParser.BlockContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_elsestmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitElsestmt" ):
                return visitor.visitElsestmt(self)
            else:
                return visitor.visitChildren(self)




    def elsestmt(self):

        localctx = MiniGoParser.ElsestmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 84, self.RULE_elsestmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 498
            self.match(MiniGoParser.KW_ELSE)
            self.state = 499
            self.block()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DatatypeforContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def KW_INT(self):
            return self.getToken(MiniGoParser.KW_INT, 0)

        def KW_FLOAT(self):
            return self.getToken(MiniGoParser.KW_FLOAT, 0)

        def KW_STRING(self):
            return self.getToken(MiniGoParser.KW_STRING, 0)

        def KW_BOOLEAN(self):
            return self.getToken(MiniGoParser.KW_BOOLEAN, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_datatypefor

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDatatypefor" ):
                return visitor.visitDatatypefor(self)
            else:
                return visitor.visitChildren(self)




    def datatypefor(self):

        localctx = MiniGoParser.DatatypeforContext(self, self._ctx, self.state)
        self.enterRule(localctx, 86, self.RULE_datatypefor)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 501
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.KW_STRING) | (1 << MiniGoParser.KW_INT) | (1 << MiniGoParser.KW_FLOAT) | (1 << MiniGoParser.KW_BOOLEAN))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VardeclforContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def KW_VAR(self):
            return self.getToken(MiniGoParser.KW_VAR, 0)

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def datatypefor(self):
            return self.getTypedRuleContext(MiniGoParser.DatatypeforContext,0)


        def ASSIGN(self):
            return self.getToken(MiniGoParser.ASSIGN, 0)

        def expr(self):
            return self.getTypedRuleContext(MiniGoParser.ExprContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_vardeclfor

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVardeclfor" ):
                return visitor.visitVardeclfor(self)
            else:
                return visitor.visitChildren(self)




    def vardeclfor(self):

        localctx = MiniGoParser.VardeclforContext(self, self._ctx, self.state)
        self.enterRule(localctx, 88, self.RULE_vardeclfor)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 503
            self.match(MiniGoParser.KW_VAR)
            self.state = 504
            self.match(MiniGoParser.ID)
            self.state = 512
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.KW_STRING, MiniGoParser.KW_INT, MiniGoParser.KW_FLOAT, MiniGoParser.KW_BOOLEAN]:
                self.state = 505
                self.datatypefor()
                self.state = 508
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==MiniGoParser.ASSIGN:
                    self.state = 506
                    self.match(MiniGoParser.ASSIGN)
                    self.state = 507
                    self.expr(0)


                pass
            elif token in [MiniGoParser.ASSIGN]:
                self.state = 510
                self.match(MiniGoParser.ASSIGN)
                self.state = 511
                self.expr(0)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LvalueforContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INT_LIT(self):
            return self.getToken(MiniGoParser.INT_LIT, 0)

        def FLOAT_LIT(self):
            return self.getToken(MiniGoParser.FLOAT_LIT, 0)

        def STRING_LIT(self):
            return self.getToken(MiniGoParser.STRING_LIT, 0)

        def KW_TRUE(self):
            return self.getToken(MiniGoParser.KW_TRUE, 0)

        def KW_FALSE(self):
            return self.getToken(MiniGoParser.KW_FALSE, 0)

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_lvaluefor

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLvaluefor" ):
                return visitor.visitLvaluefor(self)
            else:
                return visitor.visitChildren(self)




    def lvaluefor(self):

        localctx = MiniGoParser.LvalueforContext(self, self._ctx, self.state)
        self.enterRule(localctx, 90, self.RULE_lvaluefor)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 514
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.KW_TRUE) | (1 << MiniGoParser.KW_FALSE) | (1 << MiniGoParser.ID) | (1 << MiniGoParser.INT_LIT) | (1 << MiniGoParser.FLOAT_LIT) | (1 << MiniGoParser.STRING_LIT))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AssignstmtforscalarContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def lvaluefor(self):
            return self.getTypedRuleContext(MiniGoParser.LvalueforContext,0)


        def assign_op(self):
            return self.getTypedRuleContext(MiniGoParser.Assign_opContext,0)


        def expr(self):
            return self.getTypedRuleContext(MiniGoParser.ExprContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_assignstmtforscalar

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssignstmtforscalar" ):
                return visitor.visitAssignstmtforscalar(self)
            else:
                return visitor.visitChildren(self)




    def assignstmtforscalar(self):

        localctx = MiniGoParser.AssignstmtforscalarContext(self, self._ctx, self.state)
        self.enterRule(localctx, 92, self.RULE_assignstmtforscalar)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 516
            self.lvaluefor()
            self.state = 517
            self.assign_op()
            self.state = 518
            self.expr(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ForstmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return MiniGoParser.RULE_forstmt

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class ForStepContext(ForstmtContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MiniGoParser.ForstmtContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def KW_FOR(self):
            return self.getToken(MiniGoParser.KW_FOR, 0)
        def SEMI(self, i:int=None):
            if i is None:
                return self.getTokens(MiniGoParser.SEMI)
            else:
                return self.getToken(MiniGoParser.SEMI, i)
        def assignstmtforscalar(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniGoParser.AssignstmtforscalarContext)
            else:
                return self.getTypedRuleContext(MiniGoParser.AssignstmtforscalarContext,i)

        def block(self):
            return self.getTypedRuleContext(MiniGoParser.BlockContext,0)

        def vardeclfor(self):
            return self.getTypedRuleContext(MiniGoParser.VardeclforContext,0)

        def expr(self):
            return self.getTypedRuleContext(MiniGoParser.ExprContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitForStep" ):
                return visitor.visitForStep(self)
            else:
                return visitor.visitChildren(self)


    class ForBasicContext(ForstmtContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MiniGoParser.ForstmtContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def KW_FOR(self):
            return self.getToken(MiniGoParser.KW_FOR, 0)
        def expr(self):
            return self.getTypedRuleContext(MiniGoParser.ExprContext,0)

        def block(self):
            return self.getTypedRuleContext(MiniGoParser.BlockContext,0)

        def SEMI(self):
            return self.getToken(MiniGoParser.SEMI, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitForBasic" ):
                return visitor.visitForBasic(self)
            else:
                return visitor.visitChildren(self)


    class ForEachContext(ForstmtContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MiniGoParser.ForstmtContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def KW_FOR(self):
            return self.getToken(MiniGoParser.KW_FOR, 0)
        def COMMA(self):
            return self.getToken(MiniGoParser.COMMA, 0)
        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(MiniGoParser.ID)
            else:
                return self.getToken(MiniGoParser.ID, i)
        def ASSIGN_INIT(self):
            return self.getToken(MiniGoParser.ASSIGN_INIT, 0)
        def KW_RANGE(self):
            return self.getToken(MiniGoParser.KW_RANGE, 0)
        def expr(self):
            return self.getTypedRuleContext(MiniGoParser.ExprContext,0)

        def block(self):
            return self.getTypedRuleContext(MiniGoParser.BlockContext,0)

        def SEMI(self):
            return self.getToken(MiniGoParser.SEMI, 0)
        def UNDERSCORE(self):
            return self.getToken(MiniGoParser.UNDERSCORE, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitForEach" ):
                return visitor.visitForEach(self)
            else:
                return visitor.visitChildren(self)



    def forstmt(self):

        localctx = MiniGoParser.ForstmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 94, self.RULE_forstmt)
        self._la = 0 # Token type
        try:
            self.state = 549
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,48,self._ctx)
            if la_ == 1:
                localctx = MiniGoParser.ForStepContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 520
                self.match(MiniGoParser.KW_FOR)
                self.state = 523
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [MiniGoParser.KW_VAR]:
                    self.state = 521
                    self.vardeclfor()
                    pass
                elif token in [MiniGoParser.KW_TRUE, MiniGoParser.KW_FALSE, MiniGoParser.ID, MiniGoParser.INT_LIT, MiniGoParser.FLOAT_LIT, MiniGoParser.STRING_LIT]:
                    self.state = 522
                    self.assignstmtforscalar()
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 525
                self.match(MiniGoParser.SEMI)

                self.state = 526
                self.expr(0)
                self.state = 527
                self.match(MiniGoParser.SEMI)
                self.state = 528
                self.assignstmtforscalar()
                self.state = 529
                self.block()
                self.state = 530
                self.match(MiniGoParser.SEMI)
                pass

            elif la_ == 2:
                localctx = MiniGoParser.ForBasicContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 532
                self.match(MiniGoParser.KW_FOR)
                self.state = 533
                self.expr(0)
                self.state = 534
                self.block()
                self.state = 535
                self.match(MiniGoParser.SEMI)
                pass

            elif la_ == 3:
                localctx = MiniGoParser.ForEachContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 537
                self.match(MiniGoParser.KW_FOR)
                self.state = 539
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==MiniGoParser.UNDERSCORE or _la==MiniGoParser.ID:
                    self.state = 538
                    _la = self._input.LA(1)
                    if not(_la==MiniGoParser.UNDERSCORE or _la==MiniGoParser.ID):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()


                self.state = 541
                self.match(MiniGoParser.COMMA)
                self.state = 542
                self.match(MiniGoParser.ID)
                self.state = 543
                self.match(MiniGoParser.ASSIGN_INIT)
                self.state = 544
                self.match(MiniGoParser.KW_RANGE)
                self.state = 545
                self.expr(0)
                self.state = 546
                self.block()
                self.state = 547
                self.match(MiniGoParser.SEMI)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DatatypeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def arraytype(self):
            return self.getTypedRuleContext(MiniGoParser.ArraytypeContext,0)


        def primitive_type(self):
            return self.getTypedRuleContext(MiniGoParser.Primitive_typeContext,0)


        def composite_type(self):
            return self.getTypedRuleContext(MiniGoParser.Composite_typeContext,0)


        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_datatype

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDatatype" ):
                return visitor.visitDatatype(self)
            else:
                return visitor.visitChildren(self)




    def datatype(self):

        localctx = MiniGoParser.DatatypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 96, self.RULE_datatype)
        try:
            self.state = 555
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.LBRACK]:
                self.enterOuterAlt(localctx, 1)
                self.state = 551
                self.arraytype()
                pass
            elif token in [MiniGoParser.KW_STRING, MiniGoParser.KW_INT, MiniGoParser.KW_FLOAT, MiniGoParser.KW_BOOLEAN]:
                self.enterOuterAlt(localctx, 2)
                self.state = 552
                self.primitive_type()
                pass
            elif token in [MiniGoParser.KW_STRUCT, MiniGoParser.KW_INTERFACE]:
                self.enterOuterAlt(localctx, 3)
                self.state = 553
                self.composite_type()
                pass
            elif token in [MiniGoParser.ID]:
                self.enterOuterAlt(localctx, 4)
                self.state = 554
                self.match(MiniGoParser.ID)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Primitive_typeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def KW_INT(self):
            return self.getToken(MiniGoParser.KW_INT, 0)

        def KW_FLOAT(self):
            return self.getToken(MiniGoParser.KW_FLOAT, 0)

        def KW_BOOLEAN(self):
            return self.getToken(MiniGoParser.KW_BOOLEAN, 0)

        def KW_STRING(self):
            return self.getToken(MiniGoParser.KW_STRING, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_primitive_type

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPrimitive_type" ):
                return visitor.visitPrimitive_type(self)
            else:
                return visitor.visitChildren(self)




    def primitive_type(self):

        localctx = MiniGoParser.Primitive_typeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 98, self.RULE_primitive_type)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 557
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.KW_STRING) | (1 << MiniGoParser.KW_INT) | (1 << MiniGoParser.KW_FLOAT) | (1 << MiniGoParser.KW_BOOLEAN))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Composite_typeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def KW_STRUCT(self):
            return self.getToken(MiniGoParser.KW_STRUCT, 0)

        def KW_INTERFACE(self):
            return self.getToken(MiniGoParser.KW_INTERFACE, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_composite_type

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitComposite_type" ):
                return visitor.visitComposite_type(self)
            else:
                return visitor.visitChildren(self)




    def composite_type(self):

        localctx = MiniGoParser.Composite_typeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 100, self.RULE_composite_type)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 559
            _la = self._input.LA(1)
            if not(_la==MiniGoParser.KW_STRUCT or _la==MiniGoParser.KW_INTERFACE):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArraytypeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def primitive_type(self):
            return self.getTypedRuleContext(MiniGoParser.Primitive_typeContext,0)


        def composite_type(self):
            return self.getTypedRuleContext(MiniGoParser.Composite_typeContext,0)


        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(MiniGoParser.ID)
            else:
                return self.getToken(MiniGoParser.ID, i)

        def LBRACK(self, i:int=None):
            if i is None:
                return self.getTokens(MiniGoParser.LBRACK)
            else:
                return self.getToken(MiniGoParser.LBRACK, i)

        def RBRACK(self, i:int=None):
            if i is None:
                return self.getTokens(MiniGoParser.RBRACK)
            else:
                return self.getToken(MiniGoParser.RBRACK, i)

        def INT_LIT(self, i:int=None):
            if i is None:
                return self.getTokens(MiniGoParser.INT_LIT)
            else:
                return self.getToken(MiniGoParser.INT_LIT, i)

        def getRuleIndex(self):
            return MiniGoParser.RULE_arraytype

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArraytype" ):
                return visitor.visitArraytype(self)
            else:
                return visitor.visitChildren(self)




    def arraytype(self):

        localctx = MiniGoParser.ArraytypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 102, self.RULE_arraytype)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 564 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 561
                self.match(MiniGoParser.LBRACK)
                self.state = 562
                _la = self._input.LA(1)
                if not(_la==MiniGoParser.ID or _la==MiniGoParser.INT_LIT):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 563
                self.match(MiniGoParser.RBRACK)
                self.state = 566 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==MiniGoParser.LBRACK):
                    break

            self.state = 571
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.KW_STRING, MiniGoParser.KW_INT, MiniGoParser.KW_FLOAT, MiniGoParser.KW_BOOLEAN]:
                self.state = 568
                self.primitive_type()
                pass
            elif token in [MiniGoParser.KW_STRUCT, MiniGoParser.KW_INTERFACE]:
                self.state = 569
                self.composite_type()
                pass
            elif token in [MiniGoParser.ID]:
                self.state = 570
                self.match(MiniGoParser.ID)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArrayliteralContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def arraytype(self):
            return self.getTypedRuleContext(MiniGoParser.ArraytypeContext,0)


        def literalbody(self):
            return self.getTypedRuleContext(MiniGoParser.LiteralbodyContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_arrayliteral

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArrayliteral" ):
                return visitor.visitArrayliteral(self)
            else:
                return visitor.visitChildren(self)




    def arrayliteral(self):

        localctx = MiniGoParser.ArrayliteralContext(self, self._ctx, self.state)
        self.enterRule(localctx, 104, self.RULE_arrayliteral)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 573
            self.arraytype()
            self.state = 574
            self.literalbody()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LiteralbodyContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LBRACE(self):
            return self.getToken(MiniGoParser.LBRACE, 0)

        def arrayelement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniGoParser.ArrayelementContext)
            else:
                return self.getTypedRuleContext(MiniGoParser.ArrayelementContext,i)


        def RBRACE(self):
            return self.getToken(MiniGoParser.RBRACE, 0)

        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(MiniGoParser.COMMA)
            else:
                return self.getToken(MiniGoParser.COMMA, i)

        def getRuleIndex(self):
            return MiniGoParser.RULE_literalbody

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLiteralbody" ):
                return visitor.visitLiteralbody(self)
            else:
                return visitor.visitChildren(self)




    def literalbody(self):

        localctx = MiniGoParser.LiteralbodyContext(self, self._ctx, self.state)
        self.enterRule(localctx, 106, self.RULE_literalbody)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 576
            self.match(MiniGoParser.LBRACE)
            self.state = 577
            self.arrayelement()
            self.state = 582
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==MiniGoParser.COMMA:
                self.state = 578
                self.match(MiniGoParser.COMMA)
                self.state = 579
                self.arrayelement()
                self.state = 584
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 585
            self.match(MiniGoParser.RBRACE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArrayelementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def INT_LIT(self):
            return self.getToken(MiniGoParser.INT_LIT, 0)

        def FLOAT_LIT(self):
            return self.getToken(MiniGoParser.FLOAT_LIT, 0)

        def KW_TRUE(self):
            return self.getToken(MiniGoParser.KW_TRUE, 0)

        def KW_FALSE(self):
            return self.getToken(MiniGoParser.KW_FALSE, 0)

        def KW_NIL(self):
            return self.getToken(MiniGoParser.KW_NIL, 0)

        def STRING_LIT(self):
            return self.getToken(MiniGoParser.STRING_LIT, 0)

        def structliteral(self):
            return self.getTypedRuleContext(MiniGoParser.StructliteralContext,0)


        def literalbody(self):
            return self.getTypedRuleContext(MiniGoParser.LiteralbodyContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_arrayelement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArrayelement" ):
                return visitor.visitArrayelement(self)
            else:
                return visitor.visitChildren(self)




    def arrayelement(self):

        localctx = MiniGoParser.ArrayelementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 108, self.RULE_arrayelement)
        try:
            self.state = 596
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,53,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 587
                self.match(MiniGoParser.ID)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 588
                self.match(MiniGoParser.INT_LIT)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 589
                self.match(MiniGoParser.FLOAT_LIT)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 590
                self.match(MiniGoParser.KW_TRUE)
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 591
                self.match(MiniGoParser.KW_FALSE)
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 592
                self.match(MiniGoParser.KW_NIL)
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 593
                self.match(MiniGoParser.STRING_LIT)
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 594
                self.structliteral()
                pass

            elif la_ == 9:
                self.enterOuterAlt(localctx, 9)
                self.state = 595
                self.literalbody()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[21] = self.expr_sempred
        self._predicates[22] = self.expr1_sempred
        self._predicates[23] = self.expr2_sempred
        self._predicates[24] = self.expr3_sempred
        self._predicates[25] = self.expr4_sempred
        self._predicates[27] = self.expr6_sempred
        self._predicates[33] = self.lvalue_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expr_sempred(self, localctx:ExprContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 2)
         

    def expr1_sempred(self, localctx:Expr1Context, predIndex:int):
            if predIndex == 1:
                return self.precpred(self._ctx, 2)
         

    def expr2_sempred(self, localctx:Expr2Context, predIndex:int):
            if predIndex == 2:
                return self.precpred(self._ctx, 2)
         

    def expr3_sempred(self, localctx:Expr3Context, predIndex:int):
            if predIndex == 3:
                return self.precpred(self._ctx, 2)
         

    def expr4_sempred(self, localctx:Expr4Context, predIndex:int):
            if predIndex == 4:
                return self.precpred(self._ctx, 2)
         

    def expr6_sempred(self, localctx:Expr6Context, predIndex:int):
            if predIndex == 5:
                return self.precpred(self._ctx, 4)
         

            if predIndex == 6:
                return self.precpred(self._ctx, 3)
         

            if predIndex == 7:
                return self.precpred(self._ctx, 2)
         

    def lvalue_sempred(self, localctx:LvalueContext, predIndex:int):
            if predIndex == 8:
                return self.precpred(self._ctx, 2)
         

            if predIndex == 9:
                return self.precpred(self._ctx, 1)
         




