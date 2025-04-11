grammar MiniGo;
//212416
@lexer::header {
#2212416
from lexererr import *
}

@lexer::members {
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
}

options{
	language = Python3;
}

program: (decl   )+ EOF ;




// Các khai báo (declaration): bao gồm hằng số, biến, hàm, và kiểu
decl: constdecl | vardecl | funcdecl | methoddecl | typedef ;

returntype: datatype ;

// Variable declaration
vardecl: KW_VAR ID ( ( datatype (ASSIGN expr)?) | (ASSIGN expr) ) (SEMI) ;

// Const declaration
constdecl: KW_CONST ID ASSIGN expr (SEMI) ;

// Function declaration: khai báo hàm với thân được bao trong ngoặc nhọn
funcdecl: KW_FUNC ID LPAREN paramlist? RPAREN returntype? block? SEMI ;

// Built-in Functions
/*builtinfunc: 'getInt' LPAREN RPAREN   #getIntFunc
           | 'putInt' LPAREN expr RPAREN  #putIntFunc
           | 'putIntLn' LPAREN expr RPAREN  #putIntLnFunc
           | 'getFloat' LPAREN RPAREN  #getFloatFunc
           | 'putFloat' LPAREN expr RPAREN  #putFloatFunc
           | 'putFloatLn' LPAREN expr RPAREN  #putFloatLnFunc
           | 'getBool' LPAREN RPAREN  #getBoolFunc
           | 'putBool' LPAREN expr RPAREN  #putBoolFunc
           | 'putBoolLn' LPAREN expr RPAREN  #putBoolLnFunc
           | 'getString' LPAREN RPAREN  #getStringFunc
           | 'putString' LPAREN expr RPAREN  #putStringFunc
           | 'putStringLn' LPAREN expr RPAREN  #putStringLnFunc
           | 'putLn' LPAREN RPAREN  #putLnFunc
           ;
*/

// Danh sách tham số: một danh sách các tham số, phân cách bởi dấu phẩy, dùng chung function, interface
paramlist: param ( COMMA param)* ;

// Mỗi tham số: là danh sách các tên (identifierList) theo sau bởi một kiểu (datatype)
param: identifierList datatype ;
// Danh sách các identifier, cho phép nhóm tham số, ví dụ: x, y
identifierList: ID (',' ID)* ;
// Thân hàm được bao trong ngoặc nhọn
block: LBRACE stmt+ RBRACE ;

stmt: callstmt | constdecl | vardecl | ifstmt | forstmt | returnstmt | assignstmt | breakstmt | continuestmt ;
// Method declaration (có receiver)
methoddecl: KW_FUNC receiver ID LPAREN paramlist? RPAREN returntype? block SEMI ;
// Receiver: một cặp ngoặc đơn chứa tên và kiểu của receiver
receiver: LPAREN ID ID RPAREN ;

// Cập nhật định nghĩa typedef thành 2 trường hợp: struct và interface

typedef: structType | interfaceType ;

structType: KW_TYPE ID KW_STRUCT LBRACE structfields RBRACE SEMI ;
structfields: fielddecl+ ;
fielddecl: ID datatype SEMI ;

interfaceType: KW_TYPE ID KW_INTERFACE LBRACE interfaceMethodList RBRACE SEMI ;
interfaceMethodList: interfaceMethodDecl+ ;
interfaceMethodDecl: ID LPAREN paramlist? RPAREN returntype? SEMI ;

// expr '.' ID neu .expr thi ko chi rieng struct field
// Expressions for operators on different types
//foo().a.b()   
EQ      : '==' ;
NEQ     : '!=' ;
LT      : '<' ;
LE      : '<=' ;
GT      : '>' ;
GE      : '>=' ;
compare: EQ | NEQ | LT | LE | GT | GE;


expr: expr OR expr1                                    #booleanOrOp
    | expr1                                              #ex1
    ;

expr1: expr1 AND expr2                                  #booleanAndOp
     | expr2                                             #ex2
     ;

expr2: expr2 compare expr3  #relationalOp
     | expr3                                                #ex3
     ;

expr3: expr3 (PLUS | MINUS) expr4                           #mathOp1
     | expr4                                             #ex4
     ;

expr4: expr4 (MULT | DIV | MOD) expr5                     #mathOp2
     | expr5                                             #ex5
     ;

expr5: (NOT | MINUS) expr5                                  #unaryOp
     | expr6                                        #ex6
     ;

expr6: expr6 LBRACK expr RBRACK                                #arrayAccess
     | expr6 DOT ID LPAREN (expr (COMMA expr)*)? RPAREN         #methodCallexp
     | expr6 DOT ID                                      #fieldAccess
     | expr7                                                #ex7
     ;

expr7: LPAREN expr RPAREN                                      #parenExpr
     | ID LPAREN (expr (COMMA expr)*)? RPAREN #functionCallexp
     | term                                           #coban
     ;
term: ID                                                 #identifier
    | INT_LIT                                            #intLiteral
    | FLOAT_LIT                                          #floatLiteral
    | STRING_LIT                                         #stringLiteral
    | arrayliteral                                       #arrayLiteralterm
    | structliteral                                      #structLiteralterm
    | KW_TRUE                                             #trueLiteral
    | KW_FALSE                                            #falseLiteral
    | KW_NIL                                              #nilLiteral;




// Struct literal
// Một struct literal bắt đầu bằng tên kiểu (ID) theo sau là một literal body bên trong ngoặc nhọn
structliteral: ID structliteralbody ;
structliteralbody: LBRACE (fieldinit ( COMMA fieldinit)*)? RBRACE ;
fieldinit: ID COLON expr ;

// Statements
// Rule cho lvalue   scalar variable, an array element access (e.g.,arr[index]), or a struct field access
lvalue: ID | lvalue LBRACK expr RBRACK | lvalue DOT ID ;

//lvalue:            ID          | expr '[' expr ']' |   expr '.' ID     ;
//lvalue: ID | expr '.' expr ;
ASSIGN_INIT : ':=' ;
ADD_ASSIGN : '+=' ;
SUB_ASSIGN : '-=' ;
MUL_ASSIGN : '*=' ;
DIV_ASSIGN : '/=' ;
MOD_ASSIGN : '%=' ;
assign_op: ASSIGN_INIT | ADD_ASSIGN | SUB_ASSIGN | MUL_ASSIGN | DIV_ASSIGN | MOD_ASSIGN ;
// Assignment statement: cho phép lvalue ở bên trái và các toán tử gán
//assignstmt: lvalue (':=' | '+=' | '-=' | '*=' | '/=' | '%=') expr ';' ;
assignstmt: lvalue assign_op expr SEMI ;



returnstmt: KW_RETURN expr? SEMI ;
// Function and Method Calls
callstmt: ID LPAREN (expr (COMMA expr)*)? RPAREN SEMI # Functioncall
          | expr DOT ID LPAREN (expr (COMMA expr)*)? RPAREN SEMI #Methodcall // Method call luc dau:  expr '.' ID '(' (expr (',' expr)*)? ')' 
          ;// Call statement must end with semicolon or newline
// a[2].c.foo(foo(), 2);
// do array  có kiểu struct nên để array.method() nữa
breakstmt: KW_BREAK SEMI ;
continuestmt: KW_CONTINUE SEMI ;

ifstmt: KW_IF LPAREN expr RPAREN block elseifstmt* elsestmt? SEMI ;

elseifstmt: KW_ELSE KW_IF LPAREN expr RPAREN block ;

elsestmt: KW_ELSE block ;

// For Statement


// tại vardecl với assignstmt có SEMI sẵn nên sai
// chỉ scalar: int float string bool
datatypefor: KW_INT | KW_FLOAT | KW_STRING | KW_BOOLEAN;
vardeclfor: KW_VAR ID ( ( datatypefor (ASSIGN expr)?) | (ASSIGN expr) ) ;
//assignstmtfor: lvalue assign_op expr ;
lvaluefor: INT_LIT | FLOAT_LIT | STRING_LIT | KW_TRUE | KW_FALSE | ID;
assignstmtforscalar: lvaluefor assign_op expr ;

forstmt: KW_FOR  (vardeclfor | assignstmtforscalar) SEMI  (expr) SEMI assignstmtforscalar  block SEMI #forStep
       | KW_FOR expr block SEMI # forBasic
       | KW_FOR (ID | UNDERSCORE)? COMMA ID ASSIGN_INIT KW_RANGE expr block SEMI # forEach ; 
// Type definitions
datatype: arraytype |primitive_type | composite_type | ID ;

primitive_type: KW_INT | KW_FLOAT | KW_BOOLEAN | KW_STRING ;
composite_type: KW_STRUCT | KW_INTERFACE ;
// array type cần xuất ra đối với trường hợp ko phải array lit lồng ngoài
arraytype: ((LBRACK (INT_LIT | ID) RBRACK)+ (primitive_type | composite_type | ID));

// Array Literal
// Một array literal bắt đầu bằng một array type, theo sau là danh sách phần tử được bao bởi cặp ngoặc nhọn.
arrayliteral: arraytype literalbody ;
literalbody: LBRACE arrayelement (COMMA arrayelement)* RBRACE ;
arrayelement: ID | INT_LIT | FLOAT_LIT | KW_TRUE | KW_FALSE | KW_NIL | STRING_LIT | structliteral  | literalbody ;
// const a = [1]int{1+1}     
// Operators
PLUS    : '+' ;
MINUS   : '-' ;
MULT    : '*' ;
DIV     : '/' ;
MOD     : '%' ;

AND     : '&&' ;
OR      : '||' ;
NOT     : '!' ;

ASSIGN  : '=' ;
DOT     : '.' ;

// Separators
SEMI: ';';
LPAREN: '(';
RPAREN: ')';
LBRACK: '[';
RBRACK: ']';
LBRACE: '{';
RBRACE: '}';

COMMA: ',';      // Dấu phẩy
UNDERSCORE: '_'; // Gạch dưới
COLON: ':';      // Dấu hai chấm

// Keywords
KW_IF: 'if';
KW_ELSE: 'else';
KW_FOR: 'for';
KW_RETURN: 'return';
KW_FUNC: 'func';
KW_TYPE: 'type';
KW_STRUCT: 'struct';
KW_INTERFACE: 'interface';
KW_STRING: 'string';
KW_INT: 'int';
KW_FLOAT: 'float';
KW_BOOLEAN: 'boolean';
KW_CONST: 'const';
KW_VAR: 'var';
KW_CONTINUE: 'continue';
KW_BREAK: 'break';
KW_RANGE: 'range';
KW_NIL: 'nil';
KW_TRUE: 'true';
KW_FALSE: 'false';

NEWLINE: '\r'? '\n' ;

// Identifiers
ID: [a-zA-Z_][a-zA-Z_0-9]* ;

// Other lexer rules (e.g., operators, literals, etc.)

// Literals

INT_LIT: '0' | [1-9][0-9]* | '0b' [01]+ | '0B' [01]+ | '0o' [0-7]+ | '0O' [0-7]+ | '0x' [0-9a-fA-F]+ | '0X' [0-9a-fA-F]+ ;
FLOAT_LIT: [0-9]+ DOT [0-9]* ([eE] [+-]? [0-9]+)? ;


//STRING_LIT: '"' (ESCAPE_SEQUENCE | ~["\\])* '"'  ;
STRING_LIT: '"' (ESCAPE_SEQUENCE | ~["\n\r\\])* '"' ;


fragment ESCAPE_SEQUENCE:
      '\\n'
    | '\\t'  // Tab
    | '\\r'  // Carriage return
    | '\\"'  // Double quote
    | '\\\\' // Backslash
    ;




UNCLOSE_STRING: '"' (~[\n\\"] | '\\' [rnt"\\] )*  (EOF | '\n' | '\r\n') {
    if(len(self.text) >= 2 and self.text[-1] == '\n' and self.text[-2] == '\r'):
        raise UncloseString(self.text[0:-2])
    elif (self.text[-1] == '\n'):
        raise UncloseString(self.text[0:-1])
    else:
        raise UncloseString(self.text[0:])
};

ILLEGAL_ESCAPE: '"' (~[\n\\"] | '\\' [rnt"\\] )*  '\\' ~[rnt"\\] {
    raise IllegalEscape(self.text)
};


WS : [ \t\f]+ -> skip ;

COMMENT: '//' ~[\r\n]* -> skip ;
fragment NESTED_COMMENT: '/*' (NESTED_COMMENT | .)*? '*/' ;
MULTILINE_COMMENT: NESTED_COMMENT -> skip ;
ERROR_CHAR: . { raise ErrorToken(self.text) } ;