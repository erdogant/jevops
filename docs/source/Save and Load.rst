
Save and Load
''''''''''''''

Saving and loading models is desired as the learning proces of a model for ``jevops`` can take up to hours.
In order to accomplish this, we created two functions: function :func:`jevops.save` and function :func:`jevops.load`
Below we illustrate how to save and load models.


Saving
----------------

Saving a learned model can be done using the function :func:`jevops.save`:

.. code:: python

    import jevops

    # Load example data
    X,y_true = jevops.load_example()

    # Learn model
    model = jevops.fit_transform(X, y_true, pos_label='bad')

    Save model
    status = jevops.save(model, 'learned_model_v1')



Loading
----------------------

Loading a learned model can be done using the function :func:`jevops.load`:

.. code:: python

    import jevops

    # Load model
    model = jevops.load(model, 'learned_model_v1')

