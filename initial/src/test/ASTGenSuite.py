import unittest
from TestUtils import TestAST
from AST import *

class ASTGenSuite(unittest.TestCase):
    def test_var_decl_001(self):
        input = """
func Add(x int, y int) int {
    return sum;
}
const Add = 100;
    """
        expect = Program([
        FuncDecl("Add", 
                 [ParamDecl("x", IntType()), ParamDecl("y", IntType())],  # Danh sách tham số
                 IntType(),  # Kiểu trả về
                 Block([
                     VarDecl("sum", IntType(), BinaryOp("+", Id("x"), Id("y"))),  # Biến cục bộ
                     Return(Id("sum"))  # Lệnh return
                 ])
        ),
        ConstDecl("Add", None, IntLiteral(100))  # Khai báo hằng số bị trùng tên
    ])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 1000))
        
    

    def test_var_decl_002(self):
        input = """var b float;"""
        expect = Program([VarDecl("b", FloatType(), None)])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 502))

    def test_var_decl_003(self):
        input = """var c string;"""
        expect = Program([VarDecl("c", StringType(), None)])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 503))

    def test_var_decl_004(self):
        input = """var d boolean;"""
        expect = Program([VarDecl("d", BoolType(), None)])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 504))

    def test_var_decl_005(self):
        input = """var e int = 10;"""
        expect = Program([VarDecl("e", IntType(), IntLiteral(10))])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 505))

    def test_var_decl_006(self):
        input = """var f float = 3.14;"""
        expect = Program([VarDecl("f", FloatType(), FloatLiteral("3.14"))])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 506))

    def test_var_decl_007(self):
        input = """var g string = "hello";"""
        expect = Program([VarDecl("g", StringType(), StringLiteral("\"hello\""))])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 507))

    def test_var_decl_008(self):
        input = """var h boolean = true;"""
        expect = Program([VarDecl("h", BoolType(), BooleanLiteral(True))])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 508))

    def test_var_decl_009(self):
        input = """var i boolean = false;"""
        expect = Program([VarDecl("i", BoolType(), BooleanLiteral(False))])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 509))

    def test_var_decl_010(self):
        input = """var j = nil;"""
        expect = Program([VarDecl("j", None, NilLiteral())])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 510))
        
    def test_const_decl_001(self):
        input = """const a = 42;"""
        expect = Program([ConstDecl("a", None, IntLiteral(42))])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 511))

    def test_const_decl_002(self):
        input = """const b = 3.14;"""
        expect = Program([ConstDecl("b", None, FloatLiteral("3.14"))])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 512))

    def test_const_decl_003(self):
        input = """const c = "hello";"""
        expect = Program([ConstDecl("c", None, StringLiteral("\"hello\""))])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 513))

    def test_const_decl_004(self):
        input = """const d = true;"""
        expect = Program([ConstDecl("d", None, BooleanLiteral(True))])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 514))

    def test_const_decl_005(self):
        input = """const e = nil;"""
        expect = Program([ConstDecl("e", None, NilLiteral())])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 515))

    def test_const_decl_006(self):
        input = """const f = -10;"""
        expect = Program([ConstDecl("f", None, UnaryOp("-", IntLiteral(10)))])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 516))

    def test_const_decl_007(self):
        input = """const g = 0b1010;"""
        expect = Program([ConstDecl("g", None, IntLiteral("0b1010"))])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 517))

    def test_const_decl_008(self):
        input = """const h = [3]int{1, 2, 3};"""
        expect = Program([ConstDecl("h", None, ArrayLiteral([IntLiteral(3)], IntType(), [IntLiteral(1), IntLiteral(2), IntLiteral(3)]))])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 518))

    def test_const_decl_009(self):
        input = """const i = foo(1,2,3);"""
        expect = Program([ConstDecl("i", None, FuncCall("foo", [IntLiteral(1), IntLiteral(2), IntLiteral(3)]))])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 519))

    def test_const_decl_010(self):
        input = """const j = haha{};"""
        expect = Program([ConstDecl("j", None, StructLiteral("haha", []))])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 520))
        
    def test_const_001(self):
        input = """const x = 0b10101;"""
        expect = Program([ConstDecl("x", None, IntLiteral("0b10101"))])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 521))

    def test_const_002(self):
        input = """const y = 0o17;"""
        expect = Program([ConstDecl("y", None, IntLiteral("0o17"))])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 522))

    def test_const_003(self):
        input = """const z = 0XFF;"""
        expect = Program([ConstDecl("z", None, IntLiteral("0XFF"))])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 523))

    def test_const_004(self):
        input = """const a = 3.1415e2;"""
        expect = Program([ConstDecl("a", None, FloatLiteral("3.1415e2"))])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 524))

    def test_const_005(self):
        input = """const b = 0o52;"""
        expect = Program([ConstDecl("b", None, IntLiteral("0o52"))])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 525))

    def test_const_006(self):
        input = """const c = 0b111000;"""
        expect = Program([ConstDecl("c", None, IntLiteral("0b111000"))])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 526))

    def test_const_007(self):
        input = """const d = 1.23E-10;"""
        expect = Program([ConstDecl("d", None, FloatLiteral("1.23E-10"))])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 527))

    def test_const_008(self):
        input = """const e = 0xABCDE;"""
        expect = Program([ConstDecl("e", None, IntLiteral("0xABCDE"))])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 528))

    def test_const_009(self):
        input = """const f = 123.456;"""
        expect = Program([ConstDecl("f", None, FloatLiteral("123.456"))])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 529))

    def test_const_010(self):
        input = """const g = 0x10E;"""
        expect = Program([ConstDecl("g", None, IntLiteral("0x10E"))])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 530))
        
    def test_expr_001(self):
        input = """const x = 1 + 2 * 3;"""
        expect = Program([ConstDecl("x", None, BinaryOp("+", IntLiteral(1), BinaryOp("*", IntLiteral(2), IntLiteral(3))))])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 531))

    def test_expr_002(self):
        input = """const y = (4 - 2) / 2;"""
        expect = Program([ConstDecl("y", None, BinaryOp("/", BinaryOp("-", IntLiteral(4), IntLiteral(2)), IntLiteral(2)))])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 532))

    def test_expr_003(self):
        input = """const z = 5 % 2;"""
        expect = Program([ConstDecl("z", None, BinaryOp("%", IntLiteral(5), IntLiteral(2)))])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 533))

    def test_expr_004(self):
        input = """const a = -3 + 5;"""
        expect = Program([ConstDecl("a", None, BinaryOp("+", UnaryOp("-", IntLiteral(3)), IntLiteral(5)))])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 534))

    def test_expr_005(self):
        input = """const b = 10 > 5 && 3 < 4;"""
        expect = Program([ConstDecl("b", None, BinaryOp("&&", BinaryOp(">", IntLiteral(10), IntLiteral(5)), BinaryOp("<", IntLiteral(3), IntLiteral(4))))])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 535))

    def test_expr_006(self):
        input = """const c = 7 == 8 || 4 != 2;"""
        expect = Program([ConstDecl("c", None, BinaryOp("||", BinaryOp("==", IntLiteral(7), IntLiteral(8)), BinaryOp("!=", IntLiteral(4), IntLiteral(2))))])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 536))

    def test_expr_007(self):
        input = """const d = !(6 <= 7);"""
        expect = Program([ConstDecl("d", None, UnaryOp("!", BinaryOp("<=", IntLiteral(6), IntLiteral(7))))])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 537))

    def test_expr_008(self):
        input = """const e = a + b * (c - d);"""
        expect = Program([ConstDecl("e", None, BinaryOp("+", Id("a"), BinaryOp("*", Id("b"), BinaryOp("-", Id("c"), Id("d")))))])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 538))

    def test_expr_009(self):
        input = """const f = (1 + 2) * (3 - 4) / (5 % 2);"""
        expect = Program([ConstDecl("f", None, BinaryOp("/", BinaryOp("*", BinaryOp("+", IntLiteral(1), IntLiteral(2)), BinaryOp("-", IntLiteral(3), IntLiteral(4))), BinaryOp("%", IntLiteral(5), IntLiteral(2))))])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 539))

    def test_expr_010(self):
        input = """const g = (x && y) || !z;"""
        expect = Program([ConstDecl("g", None, BinaryOp("||", BinaryOp("&&", Id("x"), Id("y")), UnaryOp("!", Id("z"))))])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 540))


        
    def test_func_001(self):
        input = """
            func foo() int {return;}
            func foo(haha int, hehe float) {return;}
"""
        expect = Program([FuncDecl("foo",[],IntType(),Block([Return(None)])),
			FuncDecl("foo",[ParamDecl("haha",IntType()),ParamDecl("hehe",FloatType())],VoidType(),Block([Return(None)]))
		])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 541))

    def test_func_002(self):
        input = """func foo() { return; };"""
        expect = Program([FuncDecl("foo", [], VoidType(), Block([Return(None)]))])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 542))

    def test_func_003(self):
        input = """func foo(a int) { return; };"""
        expect = Program([FuncDecl("foo", [ParamDecl("a", IntType())], VoidType(), Block([Return(None)]))])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 543))

    def test_func_004(self):
        input = """func foo(a int, b float) { return; };"""
        expect = Program([FuncDecl("foo", [ParamDecl("a", IntType()), ParamDecl("b", FloatType())], VoidType(), Block([Return(None)]))])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 544))

    def test_func_005(self):
        input = """func foo() int { return 1; };"""
        expect = Program([FuncDecl("foo", [], IntType(), Block([Return(IntLiteral(1))]))])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 545))

    def test_func_006(self):
        input = """func foo(a int) float { 
                        return 2.5; 
                    }
        """
        expect = Program([FuncDecl("foo", [ParamDecl("a", IntType())], FloatType(), Block([Return(FloatLiteral("2.5"))]))])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 546))

    def test_func_007(self):
        input = """func foo(a string, b boolean) string { 
                        return "hello"; 
                        }
                """
        expect = Program([FuncDecl("foo", [ParamDecl("a", StringType()), ParamDecl("b", BoolType())], StringType(), Block([Return(StringLiteral("\"hello\""))]))])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 547))

    def test_func_008(self):
        input = """func foo() { a := 10; };"""
        expect = Program([FuncDecl("foo", [], VoidType(), Block([Assign(Id("a"), IntLiteral(10))]))])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 548))

    def test_func_009(self):
        input = """func foo(a int, b float) { a := a + 1; b := b * 2.5; };"""
        expect = Program([FuncDecl("foo", [ParamDecl("a", IntType()), ParamDecl("b", FloatType())], VoidType(), 
                         Block([Assign(Id("a"), BinaryOp("+", Id("a"), IntLiteral(1))), 
                                Assign(Id("b"), BinaryOp("*", Id("b"), FloatLiteral("2.5")))]))])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 549))

    def test_func_010(self):
        input = """func foo() {
            if (1) { 
            return; 
            } else { 
            return 2; 
            } 
            }
            """
        expect = Program([FuncDecl("foo", [], VoidType(), Block([
            If(IntLiteral(1), Block([Return(None)]), Block([Return(IntLiteral(2))]))]))])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 550))

   
    def test_struct_001(self):
        input = """
            type daylastruct struct {
                a int;
            }
"""
        expect = Program([StructType("daylastruct",[("a",IntType())],[])
		])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 551))

    def test_struct_002(self):
        input = """
            type Person struct { 
                name string; 
            }
        """
        expect = Program([
            StructType("Person", [("name", StringType())], [])
        ])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 552))

    def test_struct_003(self):
        input = """
            type Person struct { 
                name string; 
                age int; 
            }
        """
        expect = Program([
            StructType("Person", [
                ("name", StringType()), 
                ("age", IntType())
            ], [])
        ])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 553))

    def test_struct_004(self):
        input = """
            type Car struct { 
                brand string; 
                model string; 
                year int; 
            }
        """
        expect = Program([
            StructType("Car", [
                ("brand", StringType()), 
                ("model", StringType()), 
                ("year", IntType())
            ], [])
        ])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 554))

    def test_struct_005(self):
        input = """
            type Student struct { 
                id int; 
                gpa float; 
                passed boolean;
            }
        """
        expect = Program([
            StructType("Student", [
                ("id", IntType()), 
                ("gpa", FloatType()), 
                ("passed", BoolType())
            ], [])
        ])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 555))

    def test_struct_006(self):
        input = """
            type Book struct { 
                title string; 
                author string; 
                pages int; 
            }
        """
        expect = Program([
            StructType("Book", [
                ("title", StringType()), 
                ("author", StringType()), 
                ("pages", IntType())
            ], [])
        ])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 556))

    def test_struct_007(self):
        input = """
            type Rectangle struct { 
                width float; 
                height float; 
            }
        """
        expect = Program([
            StructType("Rectangle", [
                ("width", FloatType()), 
                ("height", FloatType())
            ], [])
        ])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 557))

    def test_struct_008(self):
        input = """
            type Employee struct { 
                name string; 
                salary float; 
                position string; 
            }
        """
        expect = Program([
            StructType("Employee", [
                ("name", StringType()), 
                ("salary", FloatType()), 
                ("position", StringType())
            ], [])
        ])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 558))

    def test_struct_009(self):
        input = """
            type Computer struct { 
                cpu string; 
                ram int; 
                ssd boolean; 
            }
        """
        expect = Program([
            StructType("Computer", [
                ("cpu", StringType()), 
                ("ram", IntType()), 
                ("ssd", BoolType())
            ], [])
        ])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 559))

    def test_struct_010(self):
        input = """
            type House struct { 
                address string; 
                numRooms int; 
                price float; 
            }
        """
        expect = Program([
            StructType("House", [
                ("address", StringType()), 
                ("numRooms", IntType()), 
                ("price", FloatType())
            ], [])
        ])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 560))


        
    def test_interface_001(self):
        input = """
            type Bieuthuc interface {
                Add() ;
            }
"""
        expect = Program([InterfaceType("Bieuthuc",[Prototype("Add",[],VoidType())])
		])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 561))

    def test_interface_002(self):
        input = """
            type Animal interface { 
                Speak();
            }
        """
        expect = Program([
            InterfaceType("Animal", [
                Prototype("Speak", [], VoidType())
            ])
        ])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 562))

    def test_interface_003(self):
        input = """
            type Vehicle interface { 
                Start(); 
                Stop(); 
            }
        """
        expect = Program([
            InterfaceType("Vehicle", [
                Prototype("Start", [], VoidType()), 
                Prototype("Stop", [], VoidType())
            ])
        ])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 563))

    def test_interface_004(self):
        input = """
            type Calculator interface { 
                Add(a int, b int) int; 
            }
        """
        expect = Program([
            InterfaceType("Calculator", [
                Prototype("Add", [IntType(), IntType()], IntType())
            ])
        ])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 564))

    def test_interface_005(self):
        input = """
            type Shape interface { 
                Area() float; 
                Perimeter() float;
            }
        """
        expect = Program([
            InterfaceType("Shape", [
                Prototype("Area", [], FloatType()), 
                Prototype("Perimeter", [], FloatType())
            ])
        ])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 565))

    def test_interface_006(self):
        input = """
            type Logger interface { 
                Log(message string);
            }
        """
        expect = Program([
            InterfaceType("Logger", [
                Prototype("Log", [StringType()], VoidType())
            ])
        ])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 566))

    def test_interface_007(self):
        input = """
            type Database interface { 
                Query(sql string) string;
            }
        """
        expect = Program([
            InterfaceType("Database", [
                Prototype("Query", [StringType()], StringType())
            ])
        ])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 567))

    def test_interface_008(self):
        input = """
            type AudioPlayer interface { 
                Play(track string);
                Pause();
                Stop();
            }
        """
        expect = Program([
            InterfaceType("AudioPlayer", [
                Prototype("Play", [StringType()], VoidType()),
                Prototype("Pause", [], VoidType()),
                Prototype("Stop", [], VoidType())
            ])
        ])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 568))

    def test_interface_009(self):
        input = """
            type FileHandler interface { 
                Open(filename string) boolean; 
                Close();
            }
        """
        expect = Program([
            InterfaceType("FileHandler", [
                Prototype("Open", [StringType()], BoolType()),
                Prototype("Close", [], VoidType())
            ])
        ])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 569))

    def test_interface_010(self):
        input = """
            type NetworkDevice interface { 
                Connect(address string) boolean; 
                Disconnect();
            }
        """
        expect = Program([
            InterfaceType("NetworkDevice", [
                Prototype("Connect", [StringType()], BoolType()),
                Prototype("Disconnect", [], VoidType())
            ])
        ])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 570))

    def test_if_001(self):
        input = """func main() { if (x > 0) { return; }; };"""
        expect = Program([FuncDecl("main", [], VoidType(), 
                Block([If(BinaryOp(">", Id("x"), IntLiteral(0)), Block([Return(None)]), None)]))])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 571))

   

    def test_if_002(self):
        input = """func main() { if (x > 0) { return; } else { return; }; };"""
        expect = Program([FuncDecl("main", [], VoidType(), 
                Block([If(BinaryOp(">", Id("x"), IntLiteral(0)), 
                    Block([Return(None)]), Block([Return(None)]))]))])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 572))
        
        
    def test_if_003(self):
        input = """func main() { if (x > 0) { return; } else if (x < 0) { return; }; };"""
        expect = Program([FuncDecl("main", [], VoidType(), 
                Block([If(BinaryOp(">", Id("x"), IntLiteral(0)), 
                    Block([Return(None)]), 
                    If(BinaryOp("<", Id("x"), IntLiteral(0)), Block([Return(None)]), None))]))])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 573))

    def test_if_004(self):
        input = """func main() { if (x > 0) { if (y < 5) { return; }; }; };"""
        expect = Program([FuncDecl("main", [], VoidType(), 
                Block([If(BinaryOp(">", Id("x"), IntLiteral(0)), 
                    Block([If(BinaryOp("<", Id("y"), IntLiteral(5)), Block([Return(None)]), None)]), None)]))])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 574))
    
    def test_if_005(self):
        input = """func main() { if (x == 1) { return; } else if (x == 2) { return; } else if (x == 3) { return; }; };"""
        expect = Program([
            FuncDecl("main", [], VoidType(),
                Block([
                    If(BinaryOp("==", Id("x"), IntLiteral(1)),
                        Block([Return(None)]),
                        If(BinaryOp("==", Id("x"), IntLiteral(2)),
                            Block([Return(None)]),
                            If(BinaryOp("==", Id("x"), IntLiteral(3)),
                                Block([Return(None)]), None)
                        )
                    )
                ])
            )
        ])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 575))

    
    def test_if_006(self):
        input = """func main() { if (x + y * 2 > 10) { return; }; };"""
        expect = Program([FuncDecl("main", [], VoidType(), 
                Block([If(BinaryOp(">", BinaryOp("+", Id("x"), BinaryOp("*", Id("y"), IntLiteral(2))), IntLiteral(10)), 
                    Block([Return(None)]), None)]))])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 576))
  
    def test_if_007(self):
        input = """func main() { if (x > 0) { y := 10; z := y + 1; return; }; };"""
        expect = Program([FuncDecl("main", [], VoidType(), 
                Block([If(BinaryOp(">", Id("x"), IntLiteral(0)), 
                    Block([Assign(Id("y"), IntLiteral(10)), Assign(Id("z"), BinaryOp("+", Id("y"), IntLiteral(1))), Return(None)]), None)]))])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 577))

    def test_if_008(self):
        input = """func main() { 
                        if (x > 0) {
                            y := 10; 
                        } else { 
                            z := 20; 
                        }
                    }
            """
        expect = Program([FuncDecl("main", [], VoidType(), 
                Block([If(BinaryOp(">", Id("x"), IntLiteral(0)), 
                    Block([Assign(Id("y"), IntLiteral(10))]), 
                    Block([Assign(Id("z"), IntLiteral(20))]))]))])
        
             
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 578))
        

    def test_if_009(self):
        input = """func main() { if (x > 0) { return 42; }; };"""
        expect = Program([FuncDecl("main", [], VoidType(), 
                Block([If(BinaryOp(">", Id("x"), IntLiteral(0)), 
                    Block([Return(IntLiteral(42))]), None)]))])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 579))

    def test_if_010(self):
        input = """func main() { if (x > 0) { return 1; } else { return 0; }; };"""
        expect = Program([FuncDecl("main", [], VoidType(), 
                Block([If(BinaryOp(">", Id("x"), IntLiteral(0)), 
                    Block([Return(IntLiteral(1))]), 
                    Block([Return(IntLiteral(0))]))]))])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 580))
        
    def test_591(self):
        input = """
            func (c Calculator) Add(a int, b int) int { return a + b; };
        """
        expect = Program([
            MethodDecl("c", Id("Calculator"),
                FuncDecl("Add", [ParamDecl("a", IntType()), ParamDecl("b", IntType())], 
                IntType(), Block([Return(BinaryOp("+", Id("a"), Id("b")))])))
        ])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 581))
        
    def test_592(self):
        input = """
            func (p Person) GetName() string { return "Alice"; };
        """
        expect = Program([
            MethodDecl("p", Id("Person"),
                FuncDecl("GetName", [], StringType(), Block([Return(StringLiteral("\"Alice\""))])))
        ])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 592))
        
    def test_593(self):
        input = """
            func (c Counter) Increment() { c.value := c.value + 1; };
        """
      
        expect = Program([MethodDecl("c",Id("Counter"),
                FuncDecl("Increment",[],VoidType(),Block([
                    Assign(FieldAccess(Id("c"),"value"), BinaryOp("+", FieldAccess(Id("c"),"value"), IntLiteral(1)))])))])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 593))
    def test_594(self):
        input = """
            func (s Student) SetAge(age int) { s.age := age; };
        """
        expect = Program([
            MethodDecl("s", Id("Student"),
                FuncDecl("SetAge", [ParamDecl("age", IntType())], 
                VoidType(), Block([
                    Assign(FieldAccess(Id("s"), "age"), Id("age"))
                ])))
        ])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 594))

    def test_595(self):
        input = """
            func (a Account) Deposit(amount float) { a.balance := a.balance + amount; };
        """
        expect = Program([
            MethodDecl("a", Id("Account"),
                FuncDecl("Deposit", [ParamDecl("amount", FloatType())], 
                VoidType(), Block([
                    Assign(FieldAccess(Id("a"), "balance"), 
                           BinaryOp("+", FieldAccess(Id("a"), "balance"), Id("amount")))
                ])))
        ])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 595))

    def test_596(self):
        input = """
            func (b Bank) Transfer(from string, to string, amount float) boolean { return true; };
        """
        expect = Program([
            MethodDecl("b", Id("Bank"),
                FuncDecl("Transfer", [
                    ParamDecl("\"from\"", StringType()), 
                    ParamDecl("\"to\"", StringType()), 
                    ParamDecl("amount", FloatType())
                ], BoolType(), Block([Return(BooleanLiteral(True))])))
        ])
        

    def test_597(self):
        input = """
            func (e Employee) GetSalary() float { return e.salary; };
        """
        expect = Program([
            MethodDecl("e", Id("Employee"),
                FuncDecl("GetSalary", [], FloatType(), Block([
                    Return(FieldAccess(Id("e"), "salary"))
                ])))
        ])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 597))

    def test_598(self):
        input = """
            func (p Product) ApplyDiscount(percent float) { p.price := p.price * (1 - percent / 100); };
        """
        expect = Program([
            MethodDecl("p", Id("Product"),
                FuncDecl("ApplyDiscount", [ParamDecl("percent", FloatType())], 
                VoidType(), Block([
                    Assign(FieldAccess(Id("p"), "price"), 
                           BinaryOp("*", FieldAccess(Id("p"), "price"), 
                                    BinaryOp("-", IntLiteral(1), BinaryOp("/", Id("percent"), IntLiteral(100)))))
                ])))
        ])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 598))

    def test_599(self):
        input = """
            func (o Order) GetTotal() float { return o.total; };
        """
        expect = Program([
            MethodDecl("o", Id("Order"),
                FuncDecl("GetTotal", [], FloatType(), Block([
                    Return(FieldAccess(Id("o"), "total"))
                ])))
        ])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 599))

    def test_600(self):
        input = """
            func (t Transaction) Confirm() { t.status := "confirmed"; };
        """
        expect = Program([
            MethodDecl("t", Id("Transaction"),
                FuncDecl("Confirm", [], VoidType(), Block([
                    Assign(FieldAccess(Id("t"), "status"), StringLiteral("\"confirmed\""))
                ])))
        ])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 600))

    def test_601(self):
        input = """
            func (c Car) SetSpeed(speed int) { c.speed := speed; };
        """
        expect = Program([
            MethodDecl("c", Id("Car"),
                FuncDecl("SetSpeed", [ParamDecl("speed", IntType())], 
                VoidType(), Block([
                    Assign(FieldAccess(Id("c"), "speed"), Id("speed"))
                ])))
        ])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 601))

    def test_602(self):
        input = """
            func (u User) UpdateEmail(newEmail string) { u.email := newEmail; };
        """
        expect = Program([
            MethodDecl("u", Id("User"),
                FuncDecl("UpdateEmail", [ParamDecl("newEmail", StringType())], 
                VoidType(), Block([
                    Assign(FieldAccess(Id("u"), "email"), Id("newEmail"))
                ])))
        ])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 602))

    def test_603(self):
        input = """
            func (m Manager) ApproveRequest(reqID int) { m.approved := true; };
        """
        expect = Program([
            MethodDecl("m", Id("Manager"),
                FuncDecl("ApproveRequest", [ParamDecl("reqID", IntType())], 
                VoidType(), Block([
                    Assign(FieldAccess(Id("m"), "approved"), BooleanLiteral(True))
                ])))
        ])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 603))
        
    def test_604(self):
        input = """
            const x = 100;
        """
        expect = Program([ConstDecl("x", None, IntLiteral("100"))])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 604))

    def test_605(self):
        input = """
            var y int = 42;
        """
        expect = Program([VarDecl("y", IntType(), IntLiteral("42"))])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 605))

    def test_606(self):
        input = """
            func foo() { return; };
        """
        expect = Program([
            FuncDecl("foo", [], VoidType(), Block([Return(None)]))
        ])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 606))

    def test_607(self):
        input = """
            func foo(a int, b float) { return; };
        """
        expect = Program([
            FuncDecl("foo", [ParamDecl("a", IntType()), ParamDecl("b", FloatType())], 
                     VoidType(), Block([Return(None)]))
        ])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 607))

    def test_608(self):
        input = """
            type Point struct { x int; y int; };
        """
        expect = Program([
            StructType("Point", [("x", IntType()), ("y", IntType())], [])
        ])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 608))

    def test_609(self):
        input = """
            var z = true;
        """
        expect = Program([VarDecl("z", None, BooleanLiteral(True))])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 609))

    def test_610(self):
        input = """
            func main() { print("Hello, world!"); };
        """
        expect = Program([
            FuncDecl("main", [], VoidType(), Block([
                FuncCall("print", [StringLiteral("\"Hello, world!\"")])
            ]))
        ])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 610))


    