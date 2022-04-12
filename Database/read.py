
def getProducts():
    sql = "SELECT [AdventureWorks2019].[Sales].[SalesOrderDetail].[SalesOrderID], [AdventureWorks2019].[Production].[Product].[Name] FROM [AdventureWorks2019].[Sales].[SalesOrderDetail], [AdventureWorks2019].[Production].[Product] WHERE [AdventureWorks2019].[Sales].[SalesOrderDetail].[ProductID] = [AdventureWorks2019].[Production].[Product].[ProductID] ORDER BY [SalesOrderID] ASC;"

    return sql

def getCategories():
    sql = "SELECT DISTINCT [AdventureWorks2019].[Sales].[SalesOrderDetail].[SalesOrderID], [AdventureWorks2019].[Production].[ProductSubcategory].[Name] FROM [AdventureWorks2019].[Sales].[SalesOrderDetail], [AdventureWorks2019].[Production].[Product], [AdventureWorks2019].[Production].[ProductSubcategory] WHERE [AdventureWorks2019].[Sales].[SalesOrderDetail].[ProductID] = [AdventureWorks2019].[Production].[Product].[ProductID] AND [AdventureWorks2019].[Production].[Product].[ProductSubcategoryID] = [AdventureWorks2019].[Production].[ProductSubcategory].[ProductSubcategoryID] ORDER BY [AdventureWorks2019].[Sales].[SalesOrderDetail].[SalesOrderID] ASC;"

    return sql