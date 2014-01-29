from gluon import *

def bootstrap3(form, fields):
    form.add_class('form-horizontal')
    parent = FIELDSET()
    for id, label, controls, help in fields:
        # wrappers
        _help = SPAN(help, _class='help-block')
        # embed _help into _controls
        _controls = DIV(controls, _help, _class='col-sm-6 col-md-5 col-lg-4')
        # submit unflag by default
        _submit = False
        if isinstance(controls, INPUT):
            controls.add_class('col-sm-6 col-md-5 col-lg-4')

            if controls['_type'] == 'submit':
                # flag submit button
                _submit = True
                controls['_class'] = 'btn btn-primary'
            if controls['_type'] == 'button':
                controls['_class'] = 'btn btn-default'
            elif controls['_type'] == 'file':
                controls['_class'] = 'input-file'
            elif controls['_type'] == 'text':
                controls['_class'] = 'form-control'
            elif controls['_type'] == 'password':
                controls['_class'] = 'form-control'
            elif controls['_type'] == 'checkbox':
                controls['_class'] = 'checkbox'



        # For password fields, which are wrapped in a CAT object.
        if isinstance(controls, CAT) and isinstance(controls[0], INPUT):
            controls[0].add_class('col-sm-6 col-md-5 col-lg-4')

        if isinstance(controls, SELECT):
            controls.add_class('form-control')

        if isinstance(controls, TEXTAREA):
            controls.add_class('form-control')

        if isinstance(label, LABEL):
            label['_class'] = 'col-sm-4 col-md-3 col-lg-2 control-label'


        if _submit:
            # submit button has unwrapped label and controls, different class
            parent.append(DIV(label, DIV(controls,_class="col-sm-6 col-md-5 col-lg-4 col-sm-offset-4 col-md-offset-3 col-lg-offset-2"), _class='form-group', _id=id))
            # unflag submit (possible side effect)
            _submit = False
        else:
            # unwrapped label
            parent.append(DIV(label, _controls, _class='form-group', _id=id))
    return parent
