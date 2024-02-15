-- Create the tables

CREATE TABLE Departments (
    DepartmentID INT PRIMARY KEY,
    DepartmentName VARCHAR(100) NOT NULL
);

CREATE TABLE Employees (
    EmployeeID INT PRIMARY KEY,
    DepartmentID INT,
    EmployeeName VARCHAR(100) NOT NULL,
    Position VARCHAR(100),
    Email VARCHAR(100),
    Phone VARCHAR(20),
    FOREIGN KEY (DepartmentID) REFERENCES Departments(DepartmentID)
);

CREATE TABLE Assets (
    AssetID INT PRIMARY KEY,
    AssetName VARCHAR(100) NOT NULL,
    AssetType VARCHAR(50) NOT NULL,
    SerialNumber VARCHAR(50),
    PurchaseDate DATE,
    PurchaseCost DECIMAL(10, 2),
    AssignedToEmployeeID INT,
    CONSTRAINT FK_AssignedToEmployee FOREIGN KEY (AssignedToEmployeeID) REFERENCES Employees(EmployeeID) ON DELETE SET NULL
);

CREATE TABLE AssetHistory (
    HistoryID INT PRIMARY KEY,
    AssetID INT,
    AssignedToEmployeeID INT,
    AssignmentDate DATE,
    ReturnDate DATE,
    FOREIGN KEY (AssetID) REFERENCES Assets(AssetID),
    FOREIGN KEY (AssignedToEmployeeID) REFERENCES Employees(EmployeeID)
);
