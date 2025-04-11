# Generated from main/minigo/parser/MiniGo.g4 by ANTLR 4.9.2
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .MiniGoParser import MiniGoParser
else:
    from MiniGoParser import MiniGoParser

# This class defines a complete generic visitor for a parse tree produced by MiniGoParser.

class MiniGoVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by MiniGoParser#program.
    def visitProgram(self, ctx:MiniGoParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#decl.
    def visitDecl(self, ctx:MiniGoParser.DeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#returntype.
    def visitReturntype(self, ctx:MiniGoParser.ReturntypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#vardecl.
    def visitVardecl(self, ctx:MiniGoParser.VardeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#constdecl.
    def visitConstdecl(self, ctx:MiniGoParser.ConstdeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#funcdecl.
    def visitFuncdecl(self, ctx:MiniGoParser.FuncdeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#paramlist.
    def visitParamlist(self, ctx:MiniGoParser.ParamlistContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#param.
    def visitParam(self, ctx:MiniGoParser.ParamContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#identifierList.
    def visitIdentifierList(self, ctx:MiniGoParser.IdentifierListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#block.
    def visitBlock(self, ctx:MiniGoParser.BlockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#stmt.
    def visitStmt(self, ctx:MiniGoParser.StmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#methoddecl.
    def visitMethoddecl(self, ctx:MiniGoParser.MethoddeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#receiver.
    def visitReceiver(self, ctx:MiniGoParser.ReceiverContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#typedef.
    def visitTypedef(self, ctx:MiniGoParser.TypedefContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#structType.
    def visitStructType(self, ctx:MiniGoParser.StructTypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#structfields.
    def visitStructfields(self, ctx:MiniGoParser.StructfieldsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#fielddecl.
    def visitFielddecl(self, ctx:MiniGoParser.FielddeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#interfaceType.
    def visitInterfaceType(self, ctx:MiniGoParser.InterfaceTypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#interfaceMethodList.
    def visitInterfaceMethodList(self, ctx:MiniGoParser.InterfaceMethodListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#interfaceMethodDecl.
    def visitInterfaceMethodDecl(self, ctx:MiniGoParser.InterfaceMethodDeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#compare.
    def visitCompare(self, ctx:MiniGoParser.CompareContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#booleanOrOp.
    def visitBooleanOrOp(self, ctx:MiniGoParser.BooleanOrOpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#ex1.
    def visitEx1(self, ctx:MiniGoParser.Ex1Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#booleanAndOp.
    def visitBooleanAndOp(self, ctx:MiniGoParser.BooleanAndOpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#ex2.
    def visitEx2(self, ctx:MiniGoParser.Ex2Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#ex3.
    def visitEx3(self, ctx:MiniGoParser.Ex3Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#relationalOp.
    def visitRelationalOp(self, ctx:MiniGoParser.RelationalOpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#ex4.
    def visitEx4(self, ctx:MiniGoParser.Ex4Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#mathOp1.
    def visitMathOp1(self, ctx:MiniGoParser.MathOp1Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#ex5.
    def visitEx5(self, ctx:MiniGoParser.Ex5Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#mathOp2.
    def visitMathOp2(self, ctx:MiniGoParser.MathOp2Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#unaryOp.
    def visitUnaryOp(self, ctx:MiniGoParser.UnaryOpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#ex6.
    def visitEx6(self, ctx:MiniGoParser.Ex6Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#ex7.
    def visitEx7(self, ctx:MiniGoParser.Ex7Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#fieldAccess.
    def visitFieldAccess(self, ctx:MiniGoParser.FieldAccessContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#methodCallexp.
    def visitMethodCallexp(self, ctx:MiniGoParser.MethodCallexpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#arrayAccess.
    def visitArrayAccess(self, ctx:MiniGoParser.ArrayAccessContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#parenExpr.
    def visitParenExpr(self, ctx:MiniGoParser.ParenExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#functionCallexp.
    def visitFunctionCallexp(self, ctx:MiniGoParser.FunctionCallexpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#coban.
    def visitCoban(self, ctx:MiniGoParser.CobanContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#identifier.
    def visitIdentifier(self, ctx:MiniGoParser.IdentifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#intLiteral.
    def visitIntLiteral(self, ctx:MiniGoParser.IntLiteralContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#floatLiteral.
    def visitFloatLiteral(self, ctx:MiniGoParser.FloatLiteralContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#stringLiteral.
    def visitStringLiteral(self, ctx:MiniGoParser.StringLiteralContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#arrayLiteralterm.
    def visitArrayLiteralterm(self, ctx:MiniGoParser.ArrayLiteraltermContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#structLiteralterm.
    def visitStructLiteralterm(self, ctx:MiniGoParser.StructLiteraltermContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#trueLiteral.
    def visitTrueLiteral(self, ctx:MiniGoParser.TrueLiteralContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#falseLiteral.
    def visitFalseLiteral(self, ctx:MiniGoParser.FalseLiteralContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#nilLiteral.
    def visitNilLiteral(self, ctx:MiniGoParser.NilLiteralContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#structliteral.
    def visitStructliteral(self, ctx:MiniGoParser.StructliteralContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#structliteralbody.
    def visitStructliteralbody(self, ctx:MiniGoParser.StructliteralbodyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#fieldinit.
    def visitFieldinit(self, ctx:MiniGoParser.FieldinitContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#lvalue.
    def visitLvalue(self, ctx:MiniGoParser.LvalueContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#assign_op.
    def visitAssign_op(self, ctx:MiniGoParser.Assign_opContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#assignstmt.
    def visitAssignstmt(self, ctx:MiniGoParser.AssignstmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#returnstmt.
    def visitReturnstmt(self, ctx:MiniGoParser.ReturnstmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#Functioncall.
    def visitFunctioncall(self, ctx:MiniGoParser.FunctioncallContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#Methodcall.
    def visitMethodcall(self, ctx:MiniGoParser.MethodcallContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#breakstmt.
    def visitBreakstmt(self, ctx:MiniGoParser.BreakstmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#continuestmt.
    def visitContinuestmt(self, ctx:MiniGoParser.ContinuestmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#ifstmt.
    def visitIfstmt(self, ctx:MiniGoParser.IfstmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#elseifstmt.
    def visitElseifstmt(self, ctx:MiniGoParser.ElseifstmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#elsestmt.
    def visitElsestmt(self, ctx:MiniGoParser.ElsestmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#datatypefor.
    def visitDatatypefor(self, ctx:MiniGoParser.DatatypeforContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#vardeclfor.
    def visitVardeclfor(self, ctx:MiniGoParser.VardeclforContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#lvaluefor.
    def visitLvaluefor(self, ctx:MiniGoParser.LvalueforContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#assignstmtforscalar.
    def visitAssignstmtforscalar(self, ctx:MiniGoParser.AssignstmtforscalarContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#forStep.
    def visitForStep(self, ctx:MiniGoParser.ForStepContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#forBasic.
    def visitForBasic(self, ctx:MiniGoParser.ForBasicContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#forEach.
    def visitForEach(self, ctx:MiniGoParser.ForEachContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#datatype.
    def visitDatatype(self, ctx:MiniGoParser.DatatypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#primitive_type.
    def visitPrimitive_type(self, ctx:MiniGoParser.Primitive_typeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#composite_type.
    def visitComposite_type(self, ctx:MiniGoParser.Composite_typeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#arraytype.
    def visitArraytype(self, ctx:MiniGoParser.ArraytypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#arrayliteral.
    def visitArrayliteral(self, ctx:MiniGoParser.ArrayliteralContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#literalbody.
    def visitLiteralbody(self, ctx:MiniGoParser.LiteralbodyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#arrayelement.
    def visitArrayelement(self, ctx:MiniGoParser.ArrayelementContext):
        return self.visitChildren(ctx)



del MiniGoParser