Attribute VB_Name = "Module1"
Sub Stonks():


Dim ticker As String
Dim tickerrow As Integer
Dim lastrow As Long
Dim opening As Double
Dim closing As Double
Dim yearchange As Double
Dim percent_change As Double
Dim tickervolume As Double
Dim greatestpercent_increase As Double
Dim greatestpercent_increase_ticker As String
Dim greatestpercent_decrease As Double
Dim greatestpercent_decrease_ticker As String
Dim greatest_tickervolume As Double
Dim greatest_tickervolume_ticker As String

For Each ws In Worksheets

ws.Activate
lastrow = ws.Cells(Rows.Count, "A").End(xlUp).Row

tickerrow = 0
ticker = ""
yearchange = 0
opening = 0
percent_change = 0
tickervolume = 0

For i = 2 To lastrow

ticker = Cells(i, 1).Value

If opening = 0 Then
opening = Cells(i, 3).Value

End If

tickervolume = tickervolume + Cells(i, 7).Value

If Cells(i + 1, 1).Value <> ticker Then

tickerrow = tickerrow + 1
Cells(tickerrow + 1, 9) = ticker

closing = Cells(i, 6)

yearchange = closing - opening

Cells(tickerrow + 1, 10).Value = yearchange

If yearchange > 0 Then
Cells(tickerrow + 1, 10).Interior.ColorIndex = 4

ElseIf yearchange < 0 Then

Cells(tickerrow + 1, 10).Interior.ColorIndex = 3

Else

Cells(tickerrow + 1, 10).Interior.ColorIndex = 6

End If

If opening = 0 Then
percent_change = 0

Else

percent_change = (yearchange / opening)

End If

Cells(tickerrow + 1, 11).Value = Format(percent_change, "Percent")

If percent_change > 0 Then

Cells(tickerrow + 1, 11).Interior.ColorIndex = 4

ElseIf percent_change < 0 Then

Cells(tickerrow + 1, 11).Interior.ColorIndex = 3

Else

Cells(tickerrow + 1, 11).Interior.ColorIndex = 6

End If

opening = 0

Cells(tickerrow + 1, 12).Value = tickervolume

tickervolume = 0

End If

Next i

lastrow = ws.Cells(Rows.Count, "I").End(xlUp).Row

greatestpercent_increase = Cells(2, 11).Value
greatestpercent_increase_ticker = Cells(2, 9).Value
greatestpercent_decrease = Cells(2, 11).Value
greatestpercent_decrease_ticker = Cells(2, 9).Value
greatest_tickervolume = Cells(2, 12).Value
greatest_tickervolume_ticker = Cells(2, 9).Value

For i = 2 To lastrow

If Cells(i, 11).Value > greatestpercent_increase Then
greatestpercent_increase = Cells(i, 11).Value
greatestpercent_increase_ticker = Cells(i, 9).Value

End If

If Cells(i, 11).Value < greatestpercent_decrease Then
greatestpercent_decrease = Cells(i, 11).Value

greatestpercent_decrease_ticker = Cells(i, 9).Value

End If

If Cells(i, 12).Value > greatest_tickervolume Then
greatest_tickervolume = Cells(i, 12).Value
greatest_tickervolume_ticker = Cells(i, 9).Value

End If

Next i

Range("P2").Value = Format(greatestpercent_increase_ticker, "Percent")
Range("Q2").Value = Format(greatestpercent_increase, "Percent")
Range("P3").Value = Format(greatestpercent_decrease_ticker, "Percent")
Range("Q3").Value = Format(greatestpercent_decrease, "Percent")
Range("P4").Value = greatest_tickervolume_ticker
Range("Q4").Value = greatest_tickervolume

Next ws

End Sub

