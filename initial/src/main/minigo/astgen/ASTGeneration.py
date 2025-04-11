from MiniGoVisitor import MiniGoVisitor
from MiniGoParser import MiniGoParser
from AST import *

class ASTGeneration(MiniGoVisitor):
    def visitProgram(self,ctx:MiniGoParser.ProgramContext):
        return Program([self.visit(i) for i in ctx.decl()])
    
    def visitDecl(self, ctx:MiniGoParser.DeclContext):
        return self.visit(ctx.getChild(0))

    # Visit a parse tree produced by MiniGoParser#returntype.
    def visitReturntype(self, ctx:MiniGoParser.ReturntypeContext):
        return self.visit(ctx.datatype())  # ✅ Lấy kiểu trả về từ `datatype`


    # Visit a parse tree produced by MiniGoParser#vardecl.
    def visitVardecl(self, ctx:MiniGoParser.VardeclContext):
        varName = ctx.ID().getText()  # ✅ Lấy tên biến
        
        # Kiểm tra nếu có datatype
        if ctx.datatype():
            varType = self.visit(ctx.datatype())  # ✅ Lấy kiểu dữ liệu
        else:
            varType = None  # ✅ Nếu không có, mặc định là None

        # Kiểm tra nếu có giá trị khởi tạo
        if ctx.expr():
            varInit = self.visit(ctx.expr())  # ✅ Lấy giá trị khởi tạo
        else:
            varInit = None  # ✅ Nếu không có, mặc định là None

        return VarDecl(varName, varType, varInit)  # ✅ Trả về AST


    # Visit a parse tree produced by MiniGoParser#constdecl.
    def visitConstdecl(self, ctx:MiniGoParser.ConstdeclContext):
        name = ctx.ID().getText()
        initValue = self.visit(ctx.expr())
        return ConstDecl(name, None, initValue)


    # Visit a parse tree produced by MiniGoParser#funcdecl.
    def visitFuncdecl(self, ctx: MiniGoParser.FuncdeclContext):
        name = ctx.ID().getText()  # ✅ Lấy tên hàm

        # ✅ Lấy danh sách tham số (nếu có)
        params = self.visit(ctx.paramlist()) if ctx.paramlist() else []

        # ✅ Lấy kiểu trả về (nếu có), mặc định `VoidType()`
        retType = self.visit(ctx.returntype()) if ctx.returntype() else VoidType()

        # ✅ Lấy thân hàm (nếu có), mặc định `Block([])`
        body = self.visit(ctx.block()) if ctx.block() else Block([])

        return FuncDecl(name, params, retType, body)


    # Visit a parse tree produced by MiniGoParser#paramlist.
    def visitParamlist(self, ctx: MiniGoParser.ParamlistContext):
        params = []
        for param in ctx.param():
            params.extend(self.visit(param))  # ✅ Dùng `extend()` thay vì `append()`
        return params


    # Visit a parse tree produced by MiniGoParser#param.
    def visitParam(self, ctx:MiniGoParser.ParamContext):
        paramType = self.visit(ctx.datatype())  # ✅ Lấy kiểu dữ liệu của tham số
        paramNames = [id.getText() for id in ctx.identifierList().ID()]  # ✅ Lấy danh sách ID
        return [ParamDecl(name, paramType) for name in paramNames]


    # Visit a parse tree produced by MiniGoParser#identifierList.
    def visitIdentifierList(self, ctx:MiniGoParser.IdentifierListContext):
        return [id.getText() for id in ctx.ID()]



    # Visit a parse tree produced by MiniGoParser#block.
    def visitBlock(self, ctx: MiniGoParser.BlockContext):
        stmt_list = [self.visit(stmt) for stmt in ctx.stmt()]
        stmt_list = [stmt for stmt in stmt_list if stmt is not None]  # ✅ Lọc bỏ `None`
        return Block(stmt_list)


    # Visit a parse tree produced by MiniGoParser#stmt.
    def visitStmt(self, ctx:MiniGoParser.StmtContext):
        return self.visit(ctx.getChild(0))


    # Visit a parse tree produced by MiniGoParser#methoddecl.
    def visitMethoddecl(self, ctx:MiniGoParser.MethoddeclContext):
        # ✅ Lấy thông tin receiver (tên và kiểu)
        receiver_name, receiver_type = self.visit(ctx.receiver())
        
        # ✅ Lấy tên method
        method_name = ctx.ID().getText()

        # ✅ Lấy danh sách tham số
        params = self.visit(ctx.paramlist()) if ctx.paramlist() else []

        # ✅ Lấy kiểu trả về
        return_type = self.visit(ctx.returntype()) if ctx.returntype() else VoidType()

        # ✅ Lấy thân hàm (block)
        body = self.visit(ctx.block()) if ctx.block() else Block([])

        # ✅ Tạo FuncDecl
        func_decl = FuncDecl(method_name, params, return_type, body)

        # ✅ Trả về MethodDecl
        return MethodDecl(receiver_name, receiver_type, func_decl)


    # Visit a parse tree produced by MiniGoParser#receiver.
    def visitReceiver(self, ctx:MiniGoParser.ReceiverContext):
        # ✅ Lấy tên của receiver
        receiver_name = ctx.ID(0).getText()

        # ✅ Lấy kiểu của receiver
        receiver_type = Id(ctx.ID(1).getText())  

        return receiver_name, receiver_type  # ✅ Trả về tuple (tên, kiểu)


    # Visit a parse tree produced by MiniGoParser#typedef.
    def visitTypedef(self, ctx:MiniGoParser.TypedefContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#structType.
    def visitStructType(self, ctx:MiniGoParser.StructTypeContext):
        # ✅ Lấy tên struct
        struct_name = ctx.ID().getText()

        # ✅ Lấy danh sách các trường (fields)
        elements = self.visit(ctx.structfields())

        # ✅ Danh sách method sẽ được xử lý ở phần khác
        methods = []  # Giả sử không có methods trong struct này

        # ✅ Trả về StructType
        return StructType(struct_name, elements, methods)

    # Visit a parse tree produced by MiniGoParser#structfields.
    def visitStructfields(self, ctx:MiniGoParser.StructfieldsContext):
        return [self.visit(field) for field in ctx.fielddecl()]


    # Visit a parse tree produced by MiniGoParser#fielddecl.
    def visitFielddecl(self, ctx:MiniGoParser.FielddeclContext):
        field_name = ctx.ID().getText()
        field_type = self.visit(ctx.datatype())  # ✅ Lấy kiểu dữ liệu của field
        return (field_name, field_type)  # ✅ Trả về tuple (tên field, kiểu dữ liệu)


    # Visit a parse tree produced by MiniGoParser#interfaceType.
    def visitInterfaceType(self, ctx:MiniGoParser.InterfaceTypeContext):
        # ✅ Lấy tên interface
        interface_name = ctx.ID().getText()

        # ✅ Lấy danh sách các phương thức của interface
        methods = self.visit(ctx.interfaceMethodList())

        # ✅ Trả về InterfaceType
        return InterfaceType(interface_name, methods)


    # Visit a parse tree produced by MiniGoParser#interfaceMethodList.
    def visitInterfaceMethodList(self, ctx:MiniGoParser.InterfaceMethodListContext):
        return [self.visit(method) for method in ctx.interfaceMethodDecl()]


    # Visit a parse tree produced by MiniGoParser#interfaceMethodDecl.
    def visitInterfaceMethodDecl(self, ctx:MiniGoParser.InterfaceMethodDeclContext):
        # ✅ Lấy tên phương thức
        method_name = ctx.ID().getText()

        # ✅ Lấy danh sách tham số
        #params = self.visit(ctx.paramlist()) if ctx.paramlist() else []
        # ✅ Lấy danh sách kiểu dữ liệu của tham số (chỉ lấy `parType`)
        params = [param.parType for param in self.visit(ctx.paramlist())] if ctx.paramlist() else []

        # ✅ Lấy kiểu trả về
        return_type = self.visit(ctx.returntype()) if ctx.returntype() else VoidType()

        # ✅ Trả về Prototype của phương thức
        return Prototype(method_name, params, return_type)


    # Visit a parse tree produced by MiniGoParser#compare.
    def visitCompare(self, ctx:MiniGoParser.CompareContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#booleanOrOp.
    def visitBooleanOrOp(self, ctx:MiniGoParser.BooleanOrOpContext):
        left = self.visit(ctx.expr())  # ✅ Không có chỉ mục
        right = self.visit(ctx.expr1())  # ✅ Sử dụng ctx.expr1()
        return BinaryOp("||", left, right)


    # Visit a parse tree produced by MiniGoParser#ex1.
    def visitEx1(self, ctx:MiniGoParser.Ex1Context):
        return self.visit(ctx.expr1())


    # Visit a parse tree produced by MiniGoParser#booleanAndOp.
    def visitBooleanAndOp(self, ctx:MiniGoParser.BooleanAndOpContext):
        left = self.visit(ctx.expr1())
        right = self.visit(ctx.expr2())
        return BinaryOp("&&", left, right)


    # Visit a parse tree produced by MiniGoParser#ex2.
    def visitEx2(self, ctx:MiniGoParser.Ex2Context):
        return self.visit(ctx.expr2())


    # Visit a parse tree produced by MiniGoParser#ex3.
    def visitEx3(self, ctx:MiniGoParser.Ex3Context):
        return self.visit(ctx.expr3())


    # Visit a parse tree produced by MiniGoParser#relationalOp.
    def visitRelationalOp(self, ctx:MiniGoParser.RelationalOpContext):
        left = self.visit(ctx.expr2())
        right = self.visit(ctx.expr3())
        op = ctx.compare().getText()  # Lấy toán tử từ Parse Tree
        return BinaryOp(op, left, right)



    # Visit a parse tree produced by MiniGoParser#ex4.
    def visitEx4(self, ctx:MiniGoParser.Ex4Context):
        return self.visit(ctx.expr4())

    # Visit a parse tree produced by MiniGoParser#mathOp1.
    def visitMathOp1(self, ctx:MiniGoParser.MathOp1Context):
        left = self.visit(ctx.expr3())
        right = self.visit(ctx.expr4())
        op = ctx.PLUS().getText() if ctx.PLUS() else ctx.MINUS().getText()
        return BinaryOp(op, left, right)


    # Visit a parse tree produced by MiniGoParser#ex5.
    def visitEx5(self, ctx:MiniGoParser.Ex5Context):
        return self.visit(ctx.expr5())


    # Visit a parse tree produced by MiniGoParser#mathOp2.
    def visitMathOp2(self, ctx:MiniGoParser.MathOp2Context):
        left = self.visit(ctx.expr4())
        right = self.visit(ctx.expr5())
        op = ctx.MULT().getText() if ctx.MULT() else ctx.DIV().getText() if ctx.DIV() else ctx.MOD().getText()
        return BinaryOp(op, left, right)



    # Visit a parse tree produced by MiniGoParser#unaryOp.
    def visitUnaryOp(self, ctx:MiniGoParser.UnaryOpContext):
        op = ctx.NOT().getText() if ctx.NOT() else ctx.MINUS().getText()
        expr = self.visit(ctx.expr5())
        return UnaryOp(op, expr)


    # Visit a parse tree produced by MiniGoParser#ex6.
    def visitEx6(self, ctx:MiniGoParser.Ex6Context):
        return self.visit(ctx.expr6())


    # Visit a parse tree produced by MiniGoParser#ex7.
    def visitEx7(self, ctx:MiniGoParser.Ex7Context):
        return self.visit(ctx.expr7())

    # Visit a parse tree produced by MiniGoParser#fieldAccess.
    def visitFieldAccess(self, ctx:MiniGoParser.FieldAccessContext):
        obj = self.visit(ctx.expr6())
        field = ctx.ID().getText()
        return FieldAccess(obj, field)


    # Visit a parse tree produced by MiniGoParser#arrayAccess.
    def visitArrayAccess(self, ctx:MiniGoParser.ArrayAccessContext):
        arr = self.visit(ctx.expr6())  # Lấy phần trước dấu []
        index_list = [self.visit(ctx.expr())]  # Lấy chỉ mục đầu tiên
        
        #Nếu phần trước đó cũng là một ArrayCell, ta gộp chỉ mục vào
        while isinstance(arr, ArrayCell):
            index_list = arr.idx + index_list  # Thêm index mới vào danh sách cũ
            arr = arr.arr  # Chỉ lấy phần gốc, bỏ ArrayCell lồng nhau
        
        return ArrayCell(arr, index_list)
    

    # Visit a parse tree produced by MiniGoParser#methodCallexp.
    def visitMethodCallexp(self, ctx:MiniGoParser.MethodCallexpContext):
        obj = self.visit(ctx.expr6())
        method = ctx.ID().getText()
        args = [self.visit(e) for e in ctx.expr()] if ctx.expr() else []
        return MethCall(obj, method, args)


    # Visit a parse tree produced by MiniGoParser#parenExpr.
    def visitParenExpr(self, ctx:MiniGoParser.ParenExprContext):
        return self.visit(ctx.expr())


    # Visit a parse tree produced by MiniGoParser#functionCallexp.
    def visitFunctionCallexp(self, ctx:MiniGoParser.FunctionCallexpContext):
        name = ctx.ID().getText()
        args = [self.visit(e) for e in ctx.expr()] if ctx.expr() else []
        return FuncCall(name, args)


    # Visit a parse tree produced by MiniGoParser#coban.
    def visitCoban(self, ctx:MiniGoParser.CobanContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#identifier.
    def visitIdentifier(self, ctx:MiniGoParser.IdentifierContext):
        return Id(ctx.ID().getText())


    # Visit a parse tree produced by MiniGoParser#intLiteral.
    def visitIntLiteral(self, ctx:MiniGoParser.IntLiteralContext):
        return IntLiteral(ctx.INT_LIT().getText())
        

    # Visit a parse tree produced by MiniGoParser#floatLiteral.
    def visitFloatLiteral(self, ctx:MiniGoParser.FloatLiteralContext):
        return FloatLiteral(ctx.FLOAT_LIT().getText())


    # Visit a parse tree produced by MiniGoParser#stringLiteral.
    def visitStringLiteral(self, ctx:MiniGoParser.StringLiteralContext):
        return StringLiteral(ctx.STRING_LIT().getText())


    # Visit a parse tree produced by MiniGoParser#arrayLiteralterm.
    def visitArrayLiteralterm(self, ctx:MiniGoParser.ArrayLiteraltermContext):
        return self.visit(ctx.arrayliteral())


    # Visit a parse tree produced by MiniGoParser#structLiteralterm.
    def visitStructLiteralterm(self, ctx:MiniGoParser.StructLiteraltermContext):
        return self.visit(ctx.structliteral())  # 🔹 Gọi visitStructliteral() để lấy ID và body


    # Visit a parse tree produced by MiniGoParser#trueLiteral.
    def visitTrueLiteral(self, ctx:MiniGoParser.TrueLiteralContext):
        ctx.getText()  # ✅ Gọi để tránh cảnh báo
        return BooleanLiteral(True)


    # Visit a parse tree produced by MiniGoParser#falseLiteral.
    def visitFalseLiteral(self, ctx:MiniGoParser.FalseLiteralContext):
        ctx.getText()  # ✅ Gọi để tránh cảnh báo
        return BooleanLiteral(False)


    # Visit a parse tree produced by MiniGoParser#nilLiteral.
    def visitNilLiteral(self, ctx:MiniGoParser.NilLiteralContext):
        ctx.getText()  # ✅ Gọi để tránh cảnh báo
        return NilLiteral()


    # Visit a parse tree produced by MiniGoParser#structliteral.
    def visitStructliteral(self, ctx:MiniGoParser.StructliteralContext):
        name = ctx.ID().getText()  # ✅ Lấy tên struct
        elements = self.visit(ctx.structliteralbody())  # ✅ Truy xuất fieldinit
        return StructLiteral(name, elements)


    # Visit a parse tree produced by MiniGoParser#structliteralbody.
    def visitStructliteralbody(self, ctx:MiniGoParser.StructliteralbodyContext):
        return [self.visit(field) for field in ctx.fieldinit()] if ctx.fieldinit() else []


    # Visit a parse tree produced by MiniGoParser#fieldinit.
    def visitFieldinit(self, ctx:MiniGoParser.FieldinitContext):
        field_name = ctx.ID().getText()  # ✅ Tên field
        value = self.visit(ctx.expr())  # ✅ Giá trị field
        return (field_name, value)  # ✅ Trả về tuple


    # Visit a parse tree produced by MiniGoParser#lvalue.
    def visitLvalue(self, ctx:MiniGoParser.LvalueContext):
        if ctx.ID() and not ctx.lvalue():  # ✅ Trường hợp biến thông thường
            return Id(ctx.ID().getText())

        if ctx.LBRACK():  # ✅ Trường hợp truy cập mảng `arr[index]`
            # arr = self.visit(ctx.lvalue())  # Lấy biến mảng

            # indices = [self.visit(e) for e in ctx.getTypedRuleContexts(MiniGoParser.ExprContext)]  
            # # 🟢 Gom tất cả chỉ mục `[index1, index2, ...]`

            # return ArrayCell(arr, indices) 
        
             # return ArrayCell(arr, [index])
            arr = self.visit(ctx.lvalue())  # Lấy phần trước dấu []
            index_list = [self.visit(ctx.expr())]  # Lấy chỉ mục đầu tiên
            
            #Nếu phần trước đó cũng là một ArrayCell, ta gộp chỉ mục vào
            while isinstance(arr, ArrayCell):
                index_list = arr.idx + index_list  # Thêm index mới vào danh sách cũ
                arr = arr.arr  # Chỉ lấy phần gốc, bỏ ArrayCell lồng nhau
            
            return ArrayCell(arr, index_list)

        if ctx.DOT():  # ✅ Trường hợp truy cập thuộc tính `obj.field`
            obj = self.visit(ctx.lvalue())  # Lấy đối tượng
            field = ctx.ID().getText()  # Lấy tên thuộc tính
            return FieldAccess(obj, field)

        return None  # ❌ Không khớp với bất kỳ trường hợp nào

    # Visit a parse tree produced by MiniGoParser#assign_op.
    def visitAssign_op(self, ctx:MiniGoParser.Assign_opContext):
        if ctx.ASSIGN_INIT():
            return ":="
        if ctx.ADD_ASSIGN():
            return "+="
        if ctx.SUB_ASSIGN():
            return "-="
        if ctx.MUL_ASSIGN():
            return "*="
        if ctx.DIV_ASSIGN():
            return "/="
        if ctx.MOD_ASSIGN():
            return "%="
        return None  # ❌ Không khớp với bất kỳ toán tử nào


    # Visit a parse tree produced by MiniGoParser#assignstmt.
    def visitAssignstmt(self, ctx:MiniGoParser.AssignstmtContext):
        lhs = self.visit(ctx.lvalue())  # ✅ Lấy biến cần gán
        rhs = self.visit(ctx.expr())  # ✅ Lấy giá trị cần gán
        op = self.visit(ctx.assign_op())  # ✅ Lấy toán tử gán

        if op == ":=":  # ✅ Nếu là `:=` thì gán trực tiếp
            return Assign(lhs, rhs)

        if op == "+=":  # ✅ Nếu là `+=` thì thay bằng `lhs = lhs + rhs`
            return Assign(lhs, BinaryOp("+", lhs, rhs))

        if op == "-=":  # ✅ Nếu là `-=`
            return Assign(lhs, BinaryOp("-", lhs, rhs))

        if op == "*=":  # ✅ Nếu là `*=`
            return Assign(lhs, BinaryOp("*", lhs, rhs))

        if op == "/=":  # ✅ Nếu là `/=`
            return Assign(lhs, BinaryOp("/", lhs, rhs))

        if op == "%=":  # ✅ Nếu là `%=`
            return Assign(lhs, BinaryOp("%", lhs, rhs))

        return None  # ❌ Không khớp với bất kỳ trường hợp nào


    # Visit a parse tree produced by MiniGoParser#returnstmt.
    def visitReturnstmt(self, ctx:MiniGoParser.ReturnstmtContext):
        expr = self.visit(ctx.expr()) if ctx.expr() else None  #  Nếu có `expr`, lấy giá trị; nếu không, trả về `None`
        return Return(expr)

        
    # Visit a parse tree produced by MiniGoParser#Functioncall.
    def visitFunctioncall(self, ctx:MiniGoParser.FunctioncallContext):
        func_name = ctx.ID().getText()  # 📌 Lấy tên hàm
        args = [self.visit(e) for e in ctx.expr()] if ctx.expr() else []  # 📌 Lấy danh sách tham số
        return FuncCall(func_name, args)  # 📌 Trả về FuncCall


    # Visit a parse tree produced by MiniGoParser#Methodcall.
    # def visitMethodcall(self, ctx:MiniGoParser.MethodcallContext):
    #     ids = ctx.ID()
    #     method_name = ids[-1].getText()  # Lấy tên method: "foo"

    #     # Xử lý phần trước dấu "." (có thể là mảng hoặc ID)
    #     array_base = Id(ids[0].getText())  # Lấy tên biến mảng (a)
    #     num_indices = len(ctx.LBRACK())  # Đếm số dấu []

    #     if num_indices > 0:
    #         indices = [self.visit(ctx.expr(i)) for i in range(num_indices)]  # Gom toàn bộ chỉ mục
    #         receiver = ArrayCell(array_base, indices)  # Gói tất cả chỉ mục vào 1 ArrayCell
    #     else:
    #         receiver = array_base  # Nếu không có [], chỉ là ID thường

    #     # Lấy danh sách tham số truyền vào method (tách đúng phần của foo)
    #     args = [self.visit(ctx.expr(i)) for i in range(num_indices, len(ctx.expr()))]

    #     return MethCall(receiver, method_name, args)

    def visitMethodcall(self, ctx: MiniGoParser.MethodcallContext):
        receiver = self.visit(ctx.expr(0))  # 📌 Receiver có thể là bất kỳ `expr`
        method_name = ctx.ID().getText()  # 📌 Lấy tên method
        args = [self.visit(arg) for arg in ctx.expr()[1:]] if ctx.expr() else []  # 📌 Lấy danh sách tham số
        return MethCall(receiver, method_name, args)
    
       

    # Visit a parse tree produced by MiniGoParser#breakstmt.
    def visitBreakstmt(self, ctx:MiniGoParser.BreakstmtContext):
        return Break()


    # Visit a parse tree produced by MiniGoParser#continuestmt.
    def visitContinuestmt(self, ctx:MiniGoParser.ContinuestmtContext):
        return Continue()


    # Visit a parse tree produced by MiniGoParser#ifstmt.
    def visitIfstmt(self, ctx:MiniGoParser.IfstmtContext):
        cond = self.visit(ctx.expr())  # ✅ Lấy điều kiện của `if`
        thenStmt = self.visit(ctx.block())  # ✅ Lấy block `then`

        # 🔄 Xử lý danh sách `else if`
        elseStmt = None
        if ctx.elsestmt():  # ✅ Nếu có `else`, lấy block của `else`
            elseStmt = self.visit(ctx.elsestmt().block())

        for elseif in reversed(ctx.elseifstmt()):  
            cond_elseif = self.visit(elseif.expr())  # ✅ Điều kiện `else if`
            then_elseif = self.visit(elseif.block())  # ✅ Block `then` của `else if`
            elseStmt = If(cond_elseif, then_elseif, elseStmt)  # ✅ Nối `else if` vào `elseStmt`

        return If(cond, thenStmt, elseStmt)  # ✅ Trả về AST chính xác



    # Visit a parse tree produced by MiniGoParser#elseifstmt.
    def visitElseifstmt(self, ctx:MiniGoParser.ElseifstmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#elsestmt.
    def visitElsestmt(self, ctx:MiniGoParser.ElsestmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#datatypefor.
    def visitDatatypefor(self, ctx:MiniGoParser.DatatypeforContext):
        if ctx.KW_INT():
            return IntType()  # ✅ Kiểu `int`
        if ctx.KW_FLOAT():
            return FloatType()  # ✅ Kiểu `float`
        if ctx.KW_STRING():
            return StringType()  # ✅ Kiểu `string`
        if ctx.KW_BOOLEAN():
            return BooleanType()  # ✅ Kiểu `boolean`

        return None  # ❌ Trường hợp không hợp lệ

    # Visit a parse tree produced by MiniGoParser#vardeclfor.
    def visitVardeclfor(self, ctx:MiniGoParser.VardeclforContext):
        var_name = ctx.ID().getText()  # 📌 Lấy tên biến
        var_type = self.visit(ctx.datatypefor()) if ctx.datatypefor() else None  # 📌 Lấy kiểu dữ liệu (nếu có)
        var_init = self.visit(ctx.expr()) if ctx.expr() else None  # 📌 Lấy giá trị khởi tạo (nếu có)

        return VarDecl(var_name, var_type, var_init)  # ✅ Trả về `VarDecl`
    
    # Visit a parse tree produced by MiniGoParser#lvaluefor.
    def visitLvaluefor(self, ctx:MiniGoParser.LvalueforContext):
        if ctx.ID():
            return Id(ctx.ID().getText())
        if ctx.INT_LIT():
            return IntLiteral(ctx.INT_LIT().getText())
        if ctx.FLOAT_LIT():
            return FloatLiteral(ctx.FLOAT_LIT().getText())
        if ctx.STRING_LIT():
            return StringLiteral(ctx.STRING_LIT().getText())
        if ctx.KW_TRUE():
            return BooleanLiteral(True)
        if ctx.KW_FALSE():
            return BooleanLiteral(False)
        return None  # ❌ Trường hợp không hợp lệ

    # Visit a parse tree produced by MiniGoParser#assignstmtforscalar.
    def visitAssignstmtforscalar(self, ctx:MiniGoParser.AssignstmtforscalarContext):
        lhs = self.visit(ctx.lvaluefor())  # ✅ Lấy biến gán (phải là scalar)
        rhs = self.visit(ctx.expr())  # ✅ Lấy giá trị
        op = ctx.assign_op().getText()  # ✅ Lấy toán tử gán

        if op == ":=":  # ✅ Gán bình thường
            return Assign(lhs, rhs)

        return Assign(lhs, BinaryOp(op[:-1], lhs, rhs))  # ✅ Biến `+=, -=, *=, /=, %=` thành `BinaryOp()`


    # Visit a parse tree produced by MiniGoParser#forCondition.
    def visitForBasic(self, ctx:MiniGoParser.ForBasicContext):
        cond = self.visit(ctx.expr())
        return ForBasic(cond, self.visit(ctx.block()))


    # Visit a parse tree produced by MiniGoParser#forStep.
    def visitForStep(self, ctx:MiniGoParser.ForStepContext):
        
         # ✅ Lấy `init` (biến lặp) - Có thể là `VarDecl` hoặc `Assign`
        init = self.visit(ctx.vardeclfor()) if ctx.vardeclfor() else self.visit(ctx.assignstmtforscalar(0))

        # ✅ Lấy `condition` (điều kiện lặp)
        cond = self.visit(ctx.expr()) if ctx.expr() else None

        # ✅ Lấy `update` (biểu thức cập nhật)
        assignments = ctx.assignstmtforscalar()
        update = self.visit(assignments[-1]) if assignments else None  # Lấy phần tử cuối

        return ForStep(init, cond, update, self.visit(ctx.block()))

        # init = self.visit(ctx.vardeclfor()) if ctx.vardeclfor() else (self.visit(ctx.assignstmtforscalar(0)) if ctx.assignstmtforscalar() else None)
        # cond = self.visit(ctx.expr()) if ctx.expr() else None
        # updates = [self.visit(stmt) for stmt in ctx.assignstmtforscalar()] if ctx.assignstmtforscalar() else []
        # update = updates[0] if updates else None  # Chỉ lấy phần tử đầu tiên
        # return ForStep(init, cond, update, self.visit(ctx.block()))



    # Visit a parse tree produced by MiniGoParser#forEach.
    def visitForEach(self, ctx:MiniGoParser.ForEachContext):
        idx = Id(ctx.ID(0).getText()) if ctx.ID(0) else None
        value = Id(ctx.ID(1).getText()) if len(ctx.ID()) > 1 else None
        rangeExpr = self.visit(ctx.expr())
        return ForEach(idx, value, rangeExpr, self.visit(ctx.block()))

    # Visit a parse tree produced by MiniGoParser#datatype.
    def visitDatatype(self, ctx:MiniGoParser.DatatypeContext):
        if ctx.arraytype():
            return self.visit(ctx.arraytype())
        if ctx.primitive_type():
            return self.visit(ctx.primitive_type())
        if ctx.composite_type():
            return self.visit(ctx.composite_type())
        if ctx.ID():
            return Id(ctx.ID().getText())  # ✅ Biến kiểu struct/interface
        return UnknownType()  # ✅ Tránh lỗi nếu không khớp


    # Visit a parse tree produced by MiniGoParser#primitive_type.
    def visitPrimitive_type(self, ctx:MiniGoParser.Primitive_typeContext):
        if ctx.KW_INT():
            return IntType()
        if ctx.KW_FLOAT():
            return FloatType()
        if ctx.KW_BOOLEAN():
            return BoolType()
        if ctx.KW_STRING():
            return StringType()
        return UnknownType()  # ✅ Tránh lỗi nếu không khớp


    # Visit a parse tree produced by MiniGoParser#composite_type.
    def visitComposite_type(self, ctx:MiniGoParser.Composite_typeContext):
        if ctx.KW_STRUCT():
            return StructType()
        if ctx.KW_INTERFACE():
            return InterfaceType()
        return UnknownType()  # ✅ Tránh lỗi nếu không khớp


    # Visit a parse tree produced by MiniGoParser#arraytype.
    def visitArraytype(self, ctx:MiniGoParser.ArraytypeContext):
        # ✅ Lấy danh sách kích thước (có thể là số hoặc ID)
        dimens = []
        eleType = None
        bracket_count = 0  # Đếm số `[` để xác định `dimens` và `eleType`

        for child in ctx.getChildren():
            if child.getText() == "[":  
                bracket_count += 1  # Gặp `[` thì tăng count
            elif child.getText() == "]":  
                bracket_count -= 1  # Gặp `]` thì giảm count
            elif bracket_count > 0:  # Nếu đang trong `[ ... ]` (dimens)
                if child.getText().isdigit():  # Nếu là số thì chuyển thành `IntLiteral`
                    dimens.append(IntLiteral(int(child.getText())))
                else:  # Nếu là ID thì chuyển thành `Id`
                    dimens.append(Id(child.getText()))
            else:  # Khi bracket_count == 0, đây là phần `eleType`
                if ctx.primitive_type():
                    eleType = self.visit(ctx.primitive_type())
                elif ctx.composite_type():
                    eleType = self.visit(ctx.composite_type())
                elif ctx.ID():
                    eleType = Id(child.getText())

        return ArrayType(dimens, eleType)  # ✅ Sửa lại để trả về `ArrayType`


    # Visit a parse tree produced by MiniGoParser#arrayliteral.
    def visitArrayliteral(self, ctx:MiniGoParser.ArrayliteralContext):
        # ✅ Lấy `ArrayType` thay vì `dimens, eleType` riêng lẻ
        arrayType = self.visit(ctx.arraytype())

        # ✅ Lấy danh sách giá trị từ literalbody
        value = self.visit(ctx.literalbody())

        return ArrayLiteral(arrayType.dimens, arrayType.eleType, value)  # ✅ Truy xuất `dimens` và `eleType` từ `ArrayType`


    # Visit a parse tree produced by MiniGoParser#literalbody.
    def visitLiteralbody(self, ctx:MiniGoParser.LiteralbodyContext):
        return [self.visit(elem) for elem in ctx.arrayelement()]


    # Visit a parse tree produced by MiniGoParser#arrayelement.
    def visitArrayelement(self, ctx: MiniGoParser.ArrayelementContext):
        if ctx.ID():
            return Id(ctx.ID().getText())
        if ctx.INT_LIT():
            return IntLiteral(ctx.INT_LIT().getText())
        if ctx.FLOAT_LIT():
            return FloatLiteral(ctx.FLOAT_LIT().getText())
        if ctx.STRING_LIT():
            return StringLiteral(ctx.STRING_LIT().getText())
        if ctx.KW_TRUE():
            return BooleanLiteral(True)
        if ctx.KW_FALSE():
            return BooleanLiteral(False)
        if ctx.KW_NIL():
            return NilLiteral()
        if ctx.structliteral():
            return self.visit(ctx.structliteral())  
        if ctx.literalbody():
            return self.visit(ctx.literalbody())  # ✅ Xử lý nested array


    
    
 

    

 
    
    
    

    



