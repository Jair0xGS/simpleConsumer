IF OBJECT_ID ( 'Cre_GeneracionCronograma', 'P' ) IS NOT NULL   
    DROP PROCEDURE Cre_GeneracionCronograma;  
GO  
CREATE PROCEDURE Cre_GeneracionCronograma
@doc char(9), @tdoc char(1), @NroCuotas smallint
AS
DECLARE @deuda numeric(9,2), @igv numeric(9,2), @tasa numeric(9,2), @cuenta smallint=0,@cuentaExiste numeric(9,2)
SET NOCOUNT ON
SELECT @cuentaExiste = count(*)
FROM DETADOC dd 
WHERE documento =@doc and tipodoc = @tdoc;

if @cuentaExiste != 0
begin
	SELECT @deuda = sum(dd.cantidad * dd.precunit) 
	FROM DETADOC dd 
	WHERE documento =@doc and tipodoc = @tdoc

	select @igv= igv/100,  @tasa= TasaInt/100 from PARAMETRO where activo =1

	SELECT @cuentaExiste = count(*)
		FROM CRONOGRAMA C
		where c.Documento= @doc and c.TipoDoc=@tdoc 
	
		if @cuentaExiste > 0
		begin
			delete from cronograma  where Documento= @doc and TipoDoc=@tdoc ;
		end


	WHILE @cuenta < @NroCuotas 
	  BEGIN
		SET @cuenta = @cuenta + 1

		INSERT CRONOGRAMA (Documento, TipoDoc, NroCuota, Importe, Interes, IgvInteres, feVence, estado)
			VALUES (@doc, @tdoc, @cuenta, @deuda/@NroCuotas, @tasa *@deuda/@NroCuotas, 
				@igv * @tasa *@deuda/@NroCuotas,   DATEADD(MM, @cuenta , GETDATE() ), 'p' )
	  END
	SELECT c.NroCuota, c.feVence, c.Importe, c.Interes, c.IgvInteres, 
	  ValorCuota = c.Importe+ c.Interes + c.IgvInteres
	FROM CRONOGRAMA C
	where c.Documento= @doc and c.TipoDoc=@tdoc 
	end
	else
	begin
	SELECT c.NroCuota, c.feVence, c.Importe, c.Interes, c.IgvInteres, 
	  ValorCuota = c.Importe+ c.Interes + c.IgvInteres
	FROM CRONOGRAMA C
	where c.Documento= '-1'
	end
	GO

CREATE PROCEDURE _RegistrarCliente
@id char(4), @zona char(2), @ruc char(11), @nombre varchar(70), @Direccion varchar(70),
@credito bit, @tipocli char(10), @saldo numeric(9,2) = 0, @Califica char(1) ='C', 
@genero char(1) = 'M', @idRepresentante int=0,  @tipo tinyint = 1
AS
IF @tipo = 1
BEGIN
       INSERT CLIENTE  (Cliente, zona, nombre, ruc, Direccion, Saldo, Credito, topeCredito,
                                TipoCliente, Calificacion, idRepresentante, genero)
       VALUES  (@id, @zona, @nombre, @ruc, @Direccion, @saldo, @credito, 0, 
                                   @tipocli, @Califica , @idRepresentante, @genero  )
END
IF @tipo = 5
       SELECT Cliente, zona, nombre, ruc, Direccion, Credito,  TipoCliente
       FROM cliente 
       WHERE nombre LIKE +  '%' +@nombre + '%'
go